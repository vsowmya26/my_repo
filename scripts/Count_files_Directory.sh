#!/bin/bash

for i in $1 ; do

	num=`ls | wc -l`

	echo "Number of files and Directories in Path "$1" is $num"
	
	echo
	
	cd $1
	
	Dir_count=`ls -lrt --file-type   | grep -e /$ | wc -l`
	
	echo "Number of Directories are $Dir_count"

	echo
	
	File_Count=$(($num - $Dir_count))
	
	echo "Number of Files are $File_Count "
done

