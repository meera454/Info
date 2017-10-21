#!/bin/bash
#set -xv
#clear
C=`top -b -n3 |awk '{print $9}' | wc -l`;top -b -n1 |grep CPU -A $C | awk '{print $1"  "$9}' > hc

python cpk.py

