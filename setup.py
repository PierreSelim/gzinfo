from setuptools import setup, find_packages

__version__ = '1.0.0'


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


setup(name='gzinfo',
      version=__version__,
      author='Pierre-Selim',
      author_email='pierre-selim@huard.info',
      url='https://github.com/PierreSelim/gzinfo',
      description='Retrieving archive filename from gz files in Python ',
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
