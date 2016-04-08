__title__ = 'mpv'
__version__ = '0.2'

from .api import MPV, api_version, load_library, load_lua
from .types import MpvLogLevel, MpvEventID
from .exceptions import MpvError
from .properties import PROPERTIES

try:
    from .pyqt import QMpv
except (ImportError, NameError):
    pass


# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
