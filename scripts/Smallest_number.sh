#!/bin/bash

echo "---This script will Identify the smallest number----"

if [[ "$#" -eq 0 ]] ; then
	echo "usage $0 <num1> <num2> ...<numN>"
	exit
fi

smallest=$1

for num in "$@" ; do

	if (( num < smallest )) ; then
		smallest=$num
	#echo "smallest number is $smallest"
													
	fi
done

 echo "smallest number is $smallest"
