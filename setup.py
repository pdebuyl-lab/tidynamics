from setuptools import setup

VERSION = '0.1.2.dev5'

with open('README.rst', 'r') as f:
    readme = f.read()

with open('tidynamics/version.py', 'w') as version_f:
    version_f.write(
        "__version__ = '{__version__}'".format(__version__=VERSION)
    )

setup(name="tidynamics",
      version=VERSION,
      description="Tiny package to compute dynamics correlations",
      long_description=readme,
      long_description_content_type="text/x-rst",
      author="Pierre de Buyl",
      author_email="pdebuyl@pdebuyl.be",
      license="BSD",
      url=" https://pypi.python.org/pypi/tidynamics",
      packages=["tidynamics"],
      install_requires=['numpy'],
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
)
