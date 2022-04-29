ECHO OFF

:q
set /P c=What game you wanna play: [Dodgy Puppy:dp / Dodgy dog:dd / Clicker game (high res):cghr / Clicker game:cg / Simon says:ss]?
if /I "%c%" EQU "dd" goto :Dog
if /I "%c%" EQU "cg" goto :Clicker
if /I "%c%" EQU "ss" goto :Simon
if /I "%c%" EQU "ddc" goto :ddc
if /I "%c%" EQU "dpc" goto :dpc
if /I "%c%" EQU "dp" goto :dp
if /I "%c%" EQU "cghr" goto :cghr
goto :q

:ddc
cd C:\Users\jackm\OneDrive\Desktop\game\Dodgy Dog
py.exe cheat.py
goto :end

:dpc
cd C:\Users\jackm\OneDrive\Desktop\game\Dodgy Puppy
py.exe cheat.py
goto :end

:dp
cd C:\Users\jackm\OneDrive\Desktop\game\Dodgy Puppy
py.exe game.py
goto :end


:Dog

cd C:\Users\jackm\OneDrive\Desktop\game\Dodgy Dog
pause
py.exe game.py
goto :end

:cghr
cd C:\Users\jackm\OneDrive\Desktop\game\clicker game (High res)
pause
py.exe game.py
goto :end


:Clicker

cd C:\Users\jackm\OneDrive\Desktop\game\clicker game
pause
py.exe game.py
goto :end

:Simon
cd C:\Users\jackm\OneDrive\Desktop\game\simon says
pause
py.exe game.py
goto :end

:end
set /P d=What wanna play more [y/n]:
if /I "%d%" EQU "y" goto :q
if /I "%d%" EQU "n" goto :stop
goto :end
pause

:stop
exit
