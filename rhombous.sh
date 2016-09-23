#!/bin/bash

echo "enter the max nummber: "
read max
echo "$max"

for (( i=1; i<=max; i++ )) # this loop is for  $max no.of iterations
do 

for (( j=max; j>=i; j-- )) #this loop is for print spaces side by side using echo -n
do
sleep 2
echo -n " " # prints space, -n not to go to new line 
done

for (( k=1; k<=i; k++ ))
do
sleep 2
echo -n  " *" ## prints star, -n not to go to new line
done
echo  ""
done
# from here reverse print

for (( i=max; i>=1; i-- ))# this loop is for  $max no.of iterations
do 

for (( j=i-1; j<=max; j++ ))#this loop is for print spaces side by side using echo -n
do
sleep 2
echo -n " " # prints space, -n not to go to new line
done

for (( k=1; k<i; k++ ))
do
sleep 2
echo -n  " *"   ## prints star, -n not to go to new line
done
echo  ""
done
