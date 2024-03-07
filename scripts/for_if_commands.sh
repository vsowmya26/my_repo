#!/bin/bash

for i in $(find .  -type f -iname "*.sh" ) 

do
	if [[ -x $i ]] ; then
		echo "$i file is  executable $(basename $i)"
	else
	     echo "$i file is not executable  "
	fi

done
	
