@ECHO OFF

SET location=%~d0%~p0

set Any=%Date:~8%
set Mes=%Date:~3,2%
set Dia=%Date:~0,2%

mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%"
mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%/Codigo Fuente"
mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%/Documentos"
mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%/Ejecutables"
mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%/Scripts"
mkdir "%cd%//Liberacion %Dia%-%Mes%-%Any%/Multimedia"

msg * "Liberacion generada satisfactoriamente!"
