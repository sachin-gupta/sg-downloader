@ECHO Calling build of documentation
CALL builddocs.bat

@ECHO This batch file will build package for this project using Sphinx
rm -rf dist/
rm -rf sg_downloader.egg-info/
@ECHO.

@ECHO Run test using unittest
REM python -m unittest tests.support.test_utilities
pytest
@ECHO.


@ECHO Building Installer for Application (Wheel)
python setup.py sdist bdist bdist_wheel --universal
