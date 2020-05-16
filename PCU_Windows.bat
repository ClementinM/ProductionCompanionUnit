@ECHO OFF
SETLOCAL
TITLE PCU Console

SET "PCU_PATH_ROOT=%CD%"
SET "PYTHONPATH=%PCU_PATH_ROOT%;%PYTHONPATH%"

python3 "./core/app/launcher.py"
REM python3 "./.tests/.test.py"

REM PAUSE