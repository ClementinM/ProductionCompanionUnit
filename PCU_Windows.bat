@ECHO OFF
SETLOCAL
TITLE PCU Console

SET "PCU_ROOT=%CD%"
SET "PYTHONPATH=%PCU_ROOT%;%PYTHONPATH%"

REM python3 "./core/launcher/main.py"
python3 ".test.py"

REM PAUSE