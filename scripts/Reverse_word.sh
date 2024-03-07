#!/bin/bash

string=$1
reverse=""
len=`expr length "$string"`
#len=$(#string)
for (( i=($len-1); i>=0; i-- )) 
    do
    reversed="$reversed${string:$i:1}"
   done 

 echo "$reversed" 

if [[ $1 ==  $reversed ]] ; then 
	echo "The word $1 is Palindrome "
else
	echo "The word $1 is not Palindrome"
fi

