@ECHO This batch file will build docs for this project using Sphinx
cd docs
rm -rf _build
call make clean
call make html
cd ..
