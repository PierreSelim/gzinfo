import os
from setuptools import setup, find_packages

__version__ = '1.0.1'


packages = sorted(find_packages())
requires = []
extra_requires = {":python_version < '3.7'": ['dataclasses']}
scripts = []
package_data = {}

# All executables are here
console_scripts = []

classifiers = [
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"]

# description
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='gzinfo',
      version=__version__,
      author='Pierre-Selim',
      author_email='pierre-selim@huard.info',
      url='https://github.com/PierreSelim/gzinfo',
      description='Retrieving archive filename from gz files in Python ',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT Licence',
      classifiers=classifiers,
      packages=packages,
      package_data=package_data,
      install_requires=requires,
      extras_require=extra_requires,
      scripts=scripts,
      entry_points={
          'console_scripts': console_scripts
      })
