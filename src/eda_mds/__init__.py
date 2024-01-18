# read version from installed package
from importlib.metadata import version
__version__ = version("eda_mds")

from eda_mds.info_na import info_na