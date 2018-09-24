#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File defines metadata, modules and packages for this distribution so that `python setup.py sdist` will create
a distribution (compressed tar file) for current project.

FEATURES:

- Packs README.md and LICENSE into the final distribution
- Packs files in MANIFEST.in into the final distribution like main.py
-
"""
# Imports for Setup Project
import io, os, sys
from shutil import rmtree
from setuptools import setup, find_packages, Command

# -------------------------------------------------------
# Packge meta-data (Mostly You'll Change Things Here Only)
# - If VERSION_OVERRIDE is none take __version__.py in root path
# - If LICENSE_OVERRIDE is none use LICENSE file in root path
# - If README.md is missins use SHORT_DESC for long_description too
# -------------------------------------------------------
NAME = 'sg-downloader'
SHORT_DESC = 'Universal course, video & url downloader'
URL_REPO = 'https://github.com/sachin-gupta/sg-downloader'
EMAIL = 'sachin.aut@gmail.com'
AUTHOR = 'Sachin Gupta'
REQUIRES_PYTHON = '>=3.6.0'
VERSION_OVERRIDE = ''
LICENSE_OVERRIDE = ''

# Packages required for this module to be executed ?
PkgREQUIRED = [
    # 'requests', 'records',
    'twine', 'git',
]

# Packages that are optional for this module to be executed ?
PkgEXTRAS = {
    # 'fancy features': ['django', 'flask'],
}

# -------------------------------------------------------
# Rest You Should'nt Have to Touch too Much
# - Except perhaps the LICENSE and related Trove Calssifiers!
# -------------------------------------------------------

# Location of this module (file path)
here = os.path.abspath(os.path.dirname(__file__))

# Import README.md and use it as long description
# - This will only work if 'README.md' is present in your 'MANIFEST.in' file
# - Generally an 'README.rst' file is required but .md will also serve the purpose
# - If README.md is missins use SHORT_DESC for long_description too
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        LONG_DESC = '\n' + f.read()
except FileNotFoundError:
        LONG_DESC = SHORT_DESC
        pass

# Import license and use it as license
# - If LICENSE_OVERRIDE is none use LICENSE file in root path
# - Faliure to load file definw simple AFGPLv3
if not LICENSE_OVERRIDE:
    try:
        with io.open(os.path.join(here, 'LICENSE'), encoding='utf-8') as f:
            LICENSE = '\n' + f.read()
    except FileNotFoundError:
            print('^^^ Warning: License Not Found, Using AFGPLv3 For Package')
            LICENSE = 'AFGPLv3'
            pass
else:
    LICENSE = LICENSE_OVERRIDE

# - If VERSION_OVERRIDE is none take __version__.py in root path
# Load the package's __version__.py as dictionary
about = {}
if not VERSION_OVERRIDE:
    with open(os.path.join(here, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION_OVERRIDE


"""
Class to implement publish command to be used as `python setup.py publish`
- This will create a universal wheel (and sdist) and uploads your package to PyPi
  using Twine, without the need for an annoying setup.cfg file.
"""
class PublishCommand(Command):
    description = 'Build universal wheel (and sdist) and upload to PyPi using Twine'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing Previous Builds ...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        try:
            self.status('Removing Previous Doc Builds ...')
            rmtree(os.path.join(here, 'docs/_build'))
        except OSError:
            pass

        self.status('Building Application Helpfiles with Sphinx ...')
        os.system('.\docs\make.bat clean')
        os.system('.\docs\make.bat html')

        self.status('Building Source Pkg, Windows Pkg & Universal Wheel Distro ...')
        os.system('{0} setup.py sdist bdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the Package to PyPI via Twine ...')
        os.system('twine upload dist/*')

        self.status('Pushing GIT Tags ...')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()
"""
HERE IS PACKAGING CONFIGURATION

- Version: Encoding the version information is an art in itself. Python packages generally adhere to the
version format major.minor[.patch][sub]. The major number is 0 for initial, experimental releases
of software. It is incremented for releases that represent major milestones in a package. The minor
number is incremented when important new features are added to the package. The patch number increments
when bug-fix releases are made. Additional trailing version information is sometimes used to indicate
sub-releases. These are “a1,a2,…,aN” (for alpha releases, where functionality and API may change), “b1,b2,…,bN”
(for beta releases, which only fix bugs) and “pr1,pr2,…,prN” (for final pre-release release testing).

- Classifier: Needs to define development status, environment, intended audience, license, operating system,
programming language, etc. These are used by build engines like Travis uses License Classifier
    - List At: https://pypi.org/pypi?%3Aaction=list_classifiers

- Packaging: Define files to be packed while making a src distribution. In present structure of the project
packages=find_packages(exclude=('tests', 'docs')) misses main.py but covers all items in source package and
its sub-packages. 'data' and 'logs' although are folder but not excluded as they're not packages not __init__.py
files shall be inside
    - packages = [] and [''] will skip main.py as well as everything under source package
    - packages = ['.', 'extrapkg'] will keep main.py as well as only extrapkg package not its child sub-packages
    - packages = ['', 'extrapkg', 'extrapkg.child1'] same as previous but sub-package child1 is included

- MANIFEST.in is able to inject extra files into the source build of this project
"""
setup(name=NAME,
    version=about['__version__'],
    license=LICENSE,

    # Description meta-data
    description=SHORT_DESC,
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    include_package_data=False,

    # Author & source ref meta-data
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    url=URL_REPO,
    download_url=URL_REPO,

    # Minimum python version
    python_requires=REQUIRES_PYTHON,

    # Packages to be added to setup
    packages=find_packages(exclude=('tests', 'docs')),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

	# entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },

    # Installation - Required Modules & Extra Modules
    install_requires=PkgREQUIRED,
    extra_requires=PkgEXTRAS,

    # Classification (Trove - List: https://pypi.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: Flask',
        'Framework :: Pytest',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
	    'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
	    'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        'Topic :: Utilities',
    ],

    # $ setup.py publish support. If call `python setup.py publish` it'll execute build all with upload ot PyPi function via twine
    cmdclass={
        'publish': PublishCommand,
    }
    )
