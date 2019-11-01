# milad teimouri 95725127

import time
import subprocess

covertData = [1,0,1,1,0,1,0,0,0,1,1,0,1,0]

print "data to send : ",''.join(str(i) for i in covertData)
print "-------------------"
command = "timeout 0.5 python covert.py"
 
for i in range(len(covertData)/2 ):
	if (int(str(covertData[i*2])+str(covertData[i*2+1]) , 2) == 0):
		while 1:
			if ( ((int(time.time())) % 10 ) in range(0,2) ):
				break;
		subprocess.call(['bash','-c', command])
		print ("00 bit sent")
		time.sleep(0.5)

	elif (int(str(covertData[i*2])+str(covertData[i*2+1]) , 2) == 1):
		while 1:
			if ( ((int(time.time())) % 10 ) in range(2,4) ):
				break;
		subprocess.call(['bash','-c', command])
		print ("01 bit sent")
		time.sleep(0.5)

	elif (int(str(covertData[i*2])+str(covertData[i*2+1]) , 2) == 2):
		while 1:
			if ( ((int(time.time())) % 10 ) in range(4,6) ):
				break;
		subprocess.call(['bash','-c', command])
		print ("10 bit sent")
		time.sleep(0.5)


	elif (int(str(covertData[i*2])+str(covertData[i*2+1]) , 2) == 3):
		while 1:
			if ( ((int(time.time())) % 10 )  in range(6,8) ):
				break;
		subprocess.call(['bash','-c', command])
		print ("11 bit sent")
		time.sleep(0.5)
	

	print "-------------------"


while 1:
	if ( ((int(time.time())) % 10 ) in range(8,10) ):
		break;
subprocess.call(['bash','-c', command])
print "EOF sent"
print "-------------------"
print "Done!"


