@echo off
rmdir %~dp0_local_env\_tmp /s /q
rmdir %~dp0_local_env\localappdata /s /q
rmdir %~dp0_local_env\userroaming\Code /s /q
mkdir %~dp0_local_env\_tmp
mkdir %~dp0_local_env\localappdata 
rem mkdir %~dp0_local_env\userprofile
rem mkdir %~dp0_local_env\userroaming
rem mkdir %~dp0_local_env\userprofile\.jupyter
rem mkdir %~dp0_local_env\userprofile\.ipython
rem mkdir %~dp0_local_env\userprofile\.matplotlib