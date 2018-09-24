@ECHO Calling build of documentation
CALL builddocs.bat

@ECHO This batch file will build package for this project using Sphinx
rm -rf dist/
rm -rf sg_downloader.egg-info/
python setup.py sdist bdist bdist_wheel --universal
