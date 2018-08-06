
from ._correlation import acf, msd, cross_displacement, correlation

try:
    from .version import __version__ as __version__
except ModuleNotFoundError as e:
    __version__ = "dev"
