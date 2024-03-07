#!/bin/bash

declare -A fruits

fruits=(
	[0]="Apple"
	[1]="Mango"
	[2]="Orange"
	[3]="Grapes"
	[4]="Banana" 
)

for i in ${fruits[4]}  ;

do 
	echo "$i"

done
