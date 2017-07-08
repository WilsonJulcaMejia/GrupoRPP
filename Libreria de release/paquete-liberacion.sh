#!/bin/bash 

#@echo off
cp ../Libreria\ de\ trabajo/Documentos/Formato\ de\ pase\ a\ produccion.xlsx Formato\ de\ pase\ a\ produccion.xlsx
#mkdir AINNI
#cd AINNI
SEPARADOR=_
NOMBRE_PROYECTO=AINNI
FECHA_ACTUAL=$(date +%d%m%Y)
#set ANIO=$FECHA_ACTUAL:~6,4$
#set MES=$FECHA_ACTUAL:~3,2$
#set DIA=$FECHA_ACTUAL:~0,2$
RUTA=$NOMBRE_PROYECTO$SEPARADOR$FECHA_ACTUAL
mkdir $RUTA
cd $RUTA
mkdir Documentos
mkdir Scripts
mkdir Ejecutable
mkdir Rollback
#exit
