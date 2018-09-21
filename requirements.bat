@ECHO OFF
@ECHO This batch file will install all python dependencies in requriements.txt and it will
@ECHO generate details of conda and pip enviornments in ./logs/ folder
REM   (Based: https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t)
REM
REM   Direct Commands:
REM     activate RStudioDevEnv
REM     conda install --yes --file requirements.txt  OR pip install -r requirements.txt
REM     deactivate 
@ECHO.
@ECHO.

@ECHO - Ensuring that ./logs/ directory exsists
mkdir ./logs
@ECHO.

@ECHO - Activating conda enviornment on local machine
call activate RStudioDevEnv

@ECHO - Verifying that RStudioDevEnv is current enviornment
@ECHO   (Also save this list to ./logs/conda_env_list.txt)
conda env list
conda env list > ./logs/conda_env_list.txt
pause
@ECHO.

@ECHO - Exporting list of pip modules to ./logs/in_pip_modules_list.txt
pip freeze > ./logs/in_pip_modules_list.txt
@ECHO.

@ECHO - Exporting conda enviornment modules to ./logs/in_conda_modules_list.txt
conda env export -n RStudioDevEnv > ./logs/in_conda_modules_list.txt
@ECHO.

@ECHO - Installing modules in requirements.txt one at a time
findstr /v /c:"#" requirements.txt > ./logs/requirements.log
FOR /f "tokens=1,2 delims=\=\=" %%A in (./logs/requirements.log) do (
  SET MODULE=%%A
  SET VERSION=%%B
  @ECHO    MODULE: %%A, VERSION: %%B
  conda install --yes %%A==%%B || pip install %%A==%%B
)
@ECHO.

@ECHO - Exporting list of pip modules to ./logs/out_pip_modules_list.txt
pip freeze > ./logs/out_pip_modules_list.txt
@ECHO.

@ECHO - Exporting conda enviornment modules to ./logs/out_conda_modules_list.txt
conda env export -n RStudioDevEnv > ./logs/out_conda_modules_list.txt
@ECHO.

@ECHO - Deactivating conda enviornment on local machine
call deactivate

@ECHO ON