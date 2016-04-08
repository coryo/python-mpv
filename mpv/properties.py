from mpv.types import MpvFormat


PROPERTIES = {
    'aid':                         (MpvFormat.INT64,  'rw'),
    'angle':                       (MpvFormat.INT64,  'rw'),
    'ass-style-override':          (MpvFormat.STRING, 'rw'),
    'ass-use-margins':             (MpvFormat.FLAG,   'rw'),
    'ass-vsfilter-aspect-compat':  (MpvFormat.FLAG,   'rw'),
    'audio':                       (MpvFormat.INT64, 'rw'), # alias for aid
    'audio-bitrate':               (MpvFormat.DOUBLE, 'r'),
    'audio-channels':              (MpvFormat.STRING, 'r'),
    'audio-codec':                 (MpvFormat.STRING, 'r'),
    'audio-delay':                 (MpvFormat.DOUBLE, 'rw'),
    'audio-format':                (MpvFormat.STRING, 'r'),
    'audio-samplerate':            (MpvFormat.INT64,  'r'),
    'avsync':                      (MpvFormat.DOUBLE, 'r'),
    'balance':                     (MpvFormat.DOUBLE, 'rw'),
    'border':                      (MpvFormat.FLAG,   'rw'),
    'brightness':                  (MpvFormat.INT64,  'rw'),
    'cache':                       (MpvFormat.INT64,  'r'),
    'cache-size':                  (MpvFormat.INT64,  'rw'),
    'chapter':                     (MpvFormat.INT64,  'rw'),
    'chapters':                    (MpvFormat.INT64,  'r'),
    'colormatrix':                 (MpvFormat.STRING, 'rw'),
    'colormatrix-input-range':     (MpvFormat.STRING, 'rw'),
    'colormatrix-output-range':    (MpvFormat.STRING, 'rw'),
    'colormatrix-primaries':       (MpvFormat.STRING, 'rw'),
    'contrast':                    (MpvFormat.INT64,  'rw'),
    'core-idle':                   (MpvFormat.FLAG,   'r'),
    'deinterlace':                 (MpvFormat.STRING, 'rw'),
    'dheight':                     (MpvFormat.INT64,  'r'),
    'disc-menu-active':            (MpvFormat.FLAG,   'r'),
    'disc-title':                  (MpvFormat.STRING, 'rw'),
    'disc-titles':                 (MpvFormat.INT64,  'r'),
    'drop-frame-count':            (MpvFormat.INT64,  'r'),
    'duration':                    (MpvFormat.DOUBLE, 'r'),
    'dwidth':                      (MpvFormat.INT64,  'r'),
    'edition':                     (MpvFormat.INT64,  'rw'),
    'editions':                    (MpvFormat.INT64,  'r'),
    'eof-reached':                 (MpvFormat.FLAG,   'r'),
    'estimated-vf-fps':            (MpvFormat.DOUBLE, 'r'),
    'file-size':                   (MpvFormat.INT64,  'r'),
    'filename':                    (MpvFormat.STRING, 'r'),
    'fps':                         (MpvFormat.DOUBLE, 'r'),
    'framedrop':                   (MpvFormat.STRING, 'rw'),
    'fullscreen':                  (MpvFormat.FLAG,   'rw'),
    'gamma':                       (MpvFormat.DOUBLE, 'rw'),
    'height':                      (MpvFormat.INT64,  'r'),
    'hr-seek':                     (MpvFormat.FLAG,   'rw'),
    'hue':                         (MpvFormat.INT64,  'rw'),
    'hwdec':                       (MpvFormat.FLAG,   'rw'),
    'idle':                        (MpvFormat.FLAG,   'r'),
    'length':                      (MpvFormat.DOUBLE, 'r'),
    'loop':                        (MpvFormat.STRING, 'rw'),
    'loop-file':                   (MpvFormat.STRING, 'rw'),
    'media-title':                 (MpvFormat.STRING, 'r'),
    'mute':                        (MpvFormat.FLAG,   'rw'),
    'ontop':                       (MpvFormat.FLAG,   'rw'),
    'osd-height':                  (MpvFormat.INT64,  'r'),
    'osd-level':                   (MpvFormat.INT64,  'rw'),
    'osd-par':                     (MpvFormat.DOUBLE, 'r'),
    'osd-scale':                   (MpvFormat.DOUBLE, 'rw'),
    'osd-width':                   (MpvFormat.INT64,   'r'),
    'panscan':                     (MpvFormat.DOUBLE, 'rw'),
    'path':                        (MpvFormat.STRING, 'r'),
    'pause':                       (MpvFormat.FLAG,   'rw'),
    'pause-for-cache':             (MpvFormat.FLAG,   'r'),
    'percent-pos':                 (MpvFormat.DOUBLE, 'rw'),
    'playback-time':               (MpvFormat.DOUBLE, 'rw'),
    'playlist-count':              (MpvFormat.INT64,  'r'),
    'playlist-pos':                (MpvFormat.INT64,  'rw'),
    'playtime-remaining':          (MpvFormat.DOUBLE, 'r'),
    'program':                     (MpvFormat.INT64,  'w'),
    'pts-association-mode':        (MpvFormat.STRING, 'rw'),
    'quvi-format':                 (MpvFormat.STRING, 'rw'),
    'ratio-pos':                   (MpvFormat.DOUBLE, 'rw'),
    'saturation':                  (MpvFormat.INT64,  'rw'),
    'secondary-sid':               (MpvFormat.STRING, 'rw'),
    'seekable':                    (MpvFormat.FLAG,   'r'),
    'sid':                         (MpvFormat.INT64, 'rw'),
    'speed':                       (MpvFormat.DOUBLE, 'rw'),
    'stream-capture':              (MpvFormat.STRING, 'rw'),
    'stream-end':                  (MpvFormat.INT64,  'r'),
    'stream-pos':                  (MpvFormat.INT64,  'rw'),
    'sub':                         (MpvFormat.INT64, 'rw'), # alias for sid
    'sub-delay':                   (MpvFormat.DOUBLE, 'rw'),
    'sub-forced-only':             (MpvFormat.FLAG,   'rw'),
    'sub-pos':                     (MpvFormat.INT64,  'rw'),
    'sub-scale':                   (MpvFormat.DOUBLE, 'rw'),
    'sub-visibility':              (MpvFormat.FLAG,   'rw'),
    'time-pos':                    (MpvFormat.DOUBLE, 'rw'),
    'time-remaining':              (MpvFormat.DOUBLE, 'r'),
    'time-start':                  (MpvFormat.DOUBLE, 'r'),
    'total-avsync-change':         (MpvFormat.DOUBLE, 'r'),
    'tv-brightness':               (MpvFormat.INT64,  'rw'),
    'tv-contrast':                 (MpvFormat.INT64,  'rw'),
    'tv-hue':                      (MpvFormat.INT64,  'rw'),
    'tv-saturation':               (MpvFormat.INT64,  'rw'),
    'vid':                         (MpvFormat.INT64,  'rw'),
    'video':                       (MpvFormat.INT64, 'rw'), # alias for vid
    'video-align-x':               (MpvFormat.DOUBLE, 'rw'),
    'video-align-y':               (MpvFormat.DOUBLE, 'rw'),
    'video-aspect':                (MpvFormat.STRING, 'rw'),
    'video-bitrate':               (MpvFormat.DOUBLE, 'r'),
    'video-codec':                 (MpvFormat.STRING, 'r'),
    'video-format':                (MpvFormat.STRING, 'r'),
    'video-pan-x':                 (MpvFormat.INT64,  'rw'),
    'video-pan-y':                 (MpvFormat.INT64,  'rw'),
    'video-unscaled':              (MpvFormat.FLAG,   'w'),
    'video-zoom':                  (MpvFormat.DOUBLE, 'rw'),
    'volume':                      (MpvFormat.DOUBLE, 'rw'),
    'width':                       (MpvFormat.INT64,  'r'),
    'window-scale':                (MpvFormat.DOUBLE, 'rw'),
    # Node Properties
    'metadata':                    (MpvFormat.NODE,   'r'),
    'chapter-metadata':            (MpvFormat.NODE,   'r'),
    'vf-metadata':                 (MpvFormat.NODE,   'r'),
    'af-metadata':                 (MpvFormat.NODE,   'r'),
    'video-params':                (MpvFormat.NODE,   'r'),
    'video-out-params':            (MpvFormat.NODE,   'r'),
    'playlist':                    (MpvFormat.NODE,   'r'),
    'track-list':                  (MpvFormat.NODE,   'r'),
    'chapter-list':                (MpvFormat.NODE,   'r'),
}