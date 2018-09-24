@ECHO Generate list of installed modules & env vars
call activate RStudioDevEnv
pip freeze > docs/pip_modules.txt
conda env export -n RStudioDevEnv > docs/conda_modules.txt
printenv > docs/printenv.txt
