@echo off
del /f %TMP%\\xxx.tmp >nul 2>nul
es -i *.gyp | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.gypi | findstr /I %__CD__% >>%TMP%\\xxx.tmp
echo File list updated.
call %~dp0gl.bat %*
