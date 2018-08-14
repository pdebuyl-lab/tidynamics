from ._correlation import acf, msd, cross_displacement, correlation
import os.path

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    __version__ = f.read().strip()
