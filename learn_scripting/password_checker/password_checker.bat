@echo off
:repeat
cls
python3 "check_pass.py"

echo.
echo Would you like to run the script again? (Y/N)
set /p choice="Enter your choice: "

if /I "%choice%"=="Y" goto repeat
if /I "%choice%"=="N" exit

echo Invalid input. Please enter Y or N.
pause
goto repeat
