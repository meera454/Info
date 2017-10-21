import os
import commands

#fh = os.system("C=`top -b -n3 |awk '{print $9}' | wc -l`;echo $C;top -b -n1 |grep CPU -A $C | awk '{print $1"  "$9}'")
cmd = "C=`top -b -n1 |awk '{print $9}' | wc -l`;echo $C;top -b -n1 |grep CPU -A $C | awk '{print $1"  "$9}'"
fh = commands.getoutput(cmd)
with open(fh, 'r') as f:
    for i in f:
        print i
