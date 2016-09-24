#!/bin/bash

echo " Enter max number: "
read max



for (( i=max; i>=1; i-- ))
do 

for (( j=i; j<=max; j++ ))
do
echo -n " ."
done

echo ""
done

#########  reverse right angle

for (( i=1; i<=max; i++ ))
do 

for (( j=max; j>=i; j-- ))
do
echo -n " ."
done

echo ""
done
