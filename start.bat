@echo off
:Main
echo.
echo.
echo Baitbot farmer
echo.
echo.
echo 1} Work
echo 2} Work and buy microchip factories
echo.
echo 3} Daily
echo 4} Daily and buy microchip factories
echo.
echo 5} [EXPIREMENTAL] Daily and work and buy microchip factories with date and time
set /p select=
if %select% EQU 1 goto 1
if %select% EQU 2 goto 2
if %select% EQU 3 goto 3
if %select% EQU 4 goto 4
if %select% EQU 4 goto 5
:1
cls
python script.py
pause
:2
cls
python scriptvar1.py
pause
:3
cls
python scriptvar2.py
pause
:4
cls
python scriptvar3.py
pause
:5
cls
python scriptvar4.py
pause