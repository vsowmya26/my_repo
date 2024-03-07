#!/bin/bash

mkdir /tmp/backup ; chmod 755 /tmp/backup

backup_dir="/tmp/backup/"
path="/home/ubuntu/scripts"
extension=".sh"

#find /home/ubuntu/ -type f -iname $extension  | while IFS= read -r file;

for file in "$path"/*"$extension" ;
do

if [[ -e $file ]] ;then

filename=$(basename -- "$file")

backupfile="${filename}_backup.sh"
cp "$file" "$backup_dir/$backupfile"

fi
	
done

