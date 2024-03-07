#!/bin/bash

if [ $# -eq 0 ] ; then
	echo "Usage is $0 <Num1> <Num2> .. <NumN>"
	exit
fi

bigger=$1

for num in "$@" ; do
	if (( num > bigger )) ; then
		bigger=$num
	fi	
done

echo "Biggest number is $bigger"
