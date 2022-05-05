@ECHO off
TITLE AL META Damage Screen Analyzer
:: set the path to the emulator screnshot folder, and the python file directories respectively
:: make sure there's no spaces on filenames
SET sc_path=D:\User\Pictures\Azur_Lane_Bluestacks
SET fl_path=C:\Users\User\folder\main.py

:: set initial count
SET /A prev_count = 0
FOR /f %%i IN ('dir %sc_path% ^| FIND "File(s)"') DO SET prev_count=%%i

:: compare number of files in screenshot dir, if number changed, execute python script
:LOOP
FOR /f %%i IN ('dir %sc_path% ^| FIND "File(s)"') DO SET curr_count=%%i
IF %prev_count% NEQ %curr_count% GOTO EXEC
GOTO WAIT

:WAIT
SET /A prev_count=%curr_count%
ECHO Waiting...
ECHO ========
ECHO Don't screenshot anything other than the META damage screen while this script is running
ECHO for less false positives, since it is monitoring the whole screenshots folder
ECHO ========
ECHO Press CTRL + C to quit, or just close the window
TIMEOUT /t 1 > nul && cls
GOTO LOOP

:EXEC
ECHO New image detected, analyzing...
:: get latest file in screenshots dir
FOR /f %%i IN ('dir %sc_path% /b/a-d/od/t:c') DO SET latest_file=%%i
:: execute python file
python -u %fl_path% -img %sc_path%\%latest_file%
PAUSE && cls
GOTO WAIT