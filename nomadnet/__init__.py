import os
import glob

from .NomadNetworkApp import NomadNetworkApp
from .ui import *


modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules if not f.endswith('__init__.py')]

def panic():
    os._exit(255)