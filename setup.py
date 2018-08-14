from setuptools import setup
import os.path

with open(os.path.join('tidynamics', 'VERSION')) as f:
    VERSION = f.read().strip()

with open('README.rst', 'r') as f:
    readme = f.read()

setup(name='tidynamics',
      version=VERSION,
      description='Tiny package to compute dynamics correlations',
      long_description=readme,
      long_description_content_type='text/x-rst',
      author='Pierre de Buyl',
      author_email='pdebuyl@pdebuyl.be',
      license='BSD',
      url='https://pypi.org/project/tidynamics/',
      packages=['tidynamics'],
      install_requires=['numpy'],
      package_data={'tidynamics': ['VERSION']},
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
)
