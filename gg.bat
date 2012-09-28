@echo off
del /f %TMP%\\xxx.tmp >nul 2>nul
es -i *.h | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.hpp | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.cpp | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.c | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.cc | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.inl | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.grd | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.idl | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.m | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.mm | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.py | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.sh | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.cfg | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i SConscript | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.scons | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.vcproj | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.vsprops | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.make | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.gyp | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.gypi | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.js | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.html | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.css | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.xcconfig | findstr /I %__CD__% >>%TMP%\\xxx.tmp
es -i *.srpc | findstr /I %__CD__% >>%TMP%\\xxx.tmp
echo File list updated.
call %~dp0gl.bat %*
