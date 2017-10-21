import signal
import commands
import os
n=None
global pid
with open("hc",'r') as h:
    for i in h:
        k = i.split()
        try:
            if k[1] >= n:
                n =k[1]
                pid = k[0]
        except:
            continue

print "HIGH CPU: ",n +"  "+ "PID: ",pid 
print "terminating the process"
PID= int(pid)
print PID

#uncomment last line to kill any PID wich eating high CPU
#Better way is set threshold value for CPU  
threshold = 25
if n >= threshold:
    os.kill(PID, 9)
    print "KILLED...."
