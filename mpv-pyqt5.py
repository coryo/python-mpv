import sys
import os
from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, QMenu, QApplication, QHBoxLayout, QSlider, QFileDialog
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QObject, QPoint
import mpv
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class QMpv(QObject):
    mpv_event = pyqtSignal()
    new_duration = pyqtSignal(int)
    playback_time = pyqtSignal(int)

    def __init__(self, wid, parent=None):
        super().__init__(parent)
        self.mpv_event.connect(self.handle_events, type=Qt.QueuedConnection)
        self.mpv = mpv.MPV(wid=wid)
        self.mpv.observe_property('track-list', mpv.MpvFormat.NODE)
        self.mpv.observe_property('playback-time', mpv.MpvFormat.DOUBLE)
        self.mpv.observe_property('duration', mpv.MpvFormat.DOUBLE)

        self.mpv.set_wakeup_callback(self.wakeup_cb)

    def quit(self):
        self.mpv.set_wakeup_callback(None)
        self.mpv.quit()

    def wakeup_cb(self, ctx):
        self.mpv_event.emit()

    @pyqtSlot()
    def handle_events(self):
        while True:
            if self.mpv is None:
                break
            try:
                event = self.mpv.wait_event(timeout=0)
                devent = event.as_dict()
            except Exception as e:
                logging.debug(e)
                break
            if devent['event_id'] == mpv.MpvEventID.NONE:
                break
            self.handle_event(devent)

    def handle_event(self, event):
        handler = {
            mpv.MpvEventID.IDLE: self.on_idle,
            mpv.MpvEventID.SHUTDOWN: self.on_shutdown,
            mpv.MpvEventID.START_FILE: self.on_start_file,
            mpv.MpvEventID.END_FILE: self.on_end_file,
            mpv.MpvEventID.PAUSE: self.on_pause,
            mpv.MpvEventID.PROPERTY_CHANGE: self.on_property_change,
            mpv.MpvEventID.LOG_MESSAGE: self.on_log_message,
            mpv.MpvEventID.FILE_LOADED: self.on_file_loaded,
            mpv.MpvEventID.TRACKS_CHANGED: self.on_tracks_changed,
            mpv.MpvEventID.METADATA_UPDATE: self.on_metadata_update
        }.get(event['event_id'], None)
        if handler is not None:
            handler(event['event'])

    def on_idle(self, event):
        pass

    def on_shutdown(self, event):
        self.mpv.detach_destroy()
        self.mpv = None

    def on_start_file(self, event):
        pass

    def on_end_file(self, event):
        pass

    def on_pause(self, event):
        pass

    def on_property_change(self, event):
        if event['data'] is None:
            return
        if event['name'] == 'playback-time':
            self.playback_time.emit(int(event['data'] * 1000))
        if event['name'] == 'duration':
            logging.debug(event)
            self.new_duration.emit(int(event['data'] * 1000))

    def on_log_message(self, event):
        pass

    def on_file_loaded(self, event):
        pass

    def on_tracks_changed(self, event):
        pass

    def on_metadata_update(self, event):
        pass

    def play(self, path):
        self.mpv.play(path)

    def seek_to(self, ms):
        self.mpv.command_node('seek', ms / 1000.0, 'absolute+exact')

    def skip(self, ms):
        self.mpv.command_node('seek', ms / 1000.0, 'relative+exact')


class PlayerControls(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.seek_bar = QSlider(orientation=Qt.Horizontal, parent=self)
        layout.addWidget(self.seek_bar)
        self.setLayout(layout)

    @pyqtSlot(int)
    def seek_bar_position(self, val):
        if not self.seek_bar.isSliderDown():
            self.seek_bar.setSliderPosition(val)


class Player(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        menu = self.menuBar().addMenu('&File')
        on_open = QAction('Open', self)
        on_open.triggered.connect(self.on_file_open)
        menu.addAction(on_open)

        self.mpv_container = QWidget(self)
        self.setCentralWidget(self.mpv_container)
        self.mpv_container.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.mpv_container.setAttribute(Qt.WA_NativeWindow)
        wid = int(self.mpv_container.winId())

        self.mpv = QMpv(wid=wid)

        self.controller = PlayerControls()
        self.controller.show()

        self.mpv.new_duration.connect(self.controller.seek_bar.setMaximum)
        self.mpv.playback_time.connect(self.controller.seek_bar_position)

        self.controller.seek_bar.sliderReleased.connect(self.slider_seek)

    @pyqtSlot()
    def on_file_open(self):
        save_file, filtr = QFileDialog.getOpenFileName(self, 'Open File')
        logging.debug(save_file)
        if save_file:
            self.mpv.play(os.path.abspath(save_file))

    @pyqtSlot()
    def slider_seek(self):
        self.mpv.seek_to(self.controller.seek_bar.value())

    def closeEvent(self, event):
        self.mpv.quit()
        self.controller.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    window.controller.move(QPoint(window.x() + window.width(), window.y()))
    sys.exit(app.exec_())
