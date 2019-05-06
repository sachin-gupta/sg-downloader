@ECHO Generate list of installed modules and env vars
call conda activate RStudioDevEnv
pip freeze > docs/pip_modules.txt
call conda env export -n RStudioDevEnv > docs/conda_modules.txt
printenv > docs/printenv.txt
call conda deactivate
