@echo off
call setenv.bat
cd /d %notebpath%
call %PYTHON_PATH%\python.exe %PYTHON_PATH%\Scripts\jupyter-lab.exe ^
--LabApp.user_settings_dir=%HOMEPATH%\.jupyterlab\lab\user-settings ^
--LabApp.workspaces_dir=%HOMEPATH%\.jupyterlab\lab\workspaces
