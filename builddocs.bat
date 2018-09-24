@ECHO This batch file will build docs for this project using Sphinx
rm -rf .\docs\_build
call .\docs\make clean
call .\docs\make html
