#!/bin/bash

file=$1

path="/home/ubuntu"

cd $path

if [[ -d "$path/backup" ]] ;then
	echo " Dircotroy exists , please copy the files"
	echo "-----------------------------------------"
	cp $1 ""$path"/backup/"$file"_$(date  +%d-%m_%H:%M)"
else
	mkdir backup; chmod 755 backup
	echo " Dircotroy create , please copy the files"
        echo "-----------------------------------------"
        cp $1 ""$path"/backup/"$file"_$(date  +%d-%m_%H:%M)"


fi
