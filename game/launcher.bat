ECHO OFF

:q
set /P c=What game you wanna play: [Dodgy dog:dd / Clicker game:cg / Clicker game (high res):cghr / Simon says:ss]?
if /I "%c%" EQU "dd" goto :Dog
if /I "%c%" EQU "cg" goto :Clicker
if /I "%c%" EQU "ss" goto :Simon
if /I "%c%" EQU "ddc" goto :ddc
if /I "%c%" EQU "cghr" goto :cghr
goto :q

:cghr
cd clicker game (High res)
py.exe game.py
goto :end

:ddc
cd Dodgy Dog
py.exe cheat.py
goto :end

:Dog

cd Dodgy Dog
pause
py.exe game.py
goto :end

:Clicker

cd clicker game
pause
py.exe game.py
goto :end

:Simon
cd simon says
pause
py.exe game.py
goto :end

:end
set /P d=What wanna play more [y/n]:
if /I "%d%" EQU "y" goto :q
if /I "%d%" EQU "n" goto :stop
pause

:stop
exit
