#!/bin/bash

path="/home/ubuntu"
extension=".csv"

for file in "$path"/*"$extension" ; do


if ! [[ -e $file ]]; then

	echo "File doesnot exist" 
	exit
fi

echo "$file has  $( cat $file | wc -l) lines init"
    	
done
