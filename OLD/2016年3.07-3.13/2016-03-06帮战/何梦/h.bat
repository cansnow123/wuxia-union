for /f "delims=" %%i in ("%cd%") do set folder=%%~ni
copy *.txt %folder%.txt