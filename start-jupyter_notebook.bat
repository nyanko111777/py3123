@echo off
call setenv.bat
cd /d %notebpath%
call %PYTHON_PATH%\python.exe %PYTHON_PATH%\Scripts\jupyter-notebook.exe
