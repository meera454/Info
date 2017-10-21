import signal
import os
n=None
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
PID= int(pid)
print PID

########################################################################################
###### NOTE: Better way is set threshold value for CPU to avoid unnecessary thing ######
######################################################################################## 
threshold = 99
N= float(n)
#print type(N) 
if N >= threshold:
    print "terminating the process"
    os.kill(PID, 9)
    print "KILLED...."
else: 
    print "No process is above the threshold"
