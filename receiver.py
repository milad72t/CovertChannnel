
import time
import subprocess
data=[]
command = 'ps -ef | grep "python covert.py" | grep -v "grep" &> /dev/null'
while 1:
	if (not subprocess.call((['bash','-c', command]))):
		time_ = time.time()
		if ( ((int(time_) % 10)) in range(0,2) ):
			data.append("00")
			print "00 bit received"
		elif (((int(time_) % 10)) in range(2,4)):
			data.append("01")
			print "01 bit received"
		elif (((int(time_) % 10)) in range(4,6)):
			data.append("10")
			print "10 bit received"
		elif (((int(time_) % 10)) in range(6,8)):
			data.append("11")
			print "11 bit received"
		elif (((int(time_) % 10)) in range(8,10)):
			print "EOF received"
			print "-------------------"
			print "received data =  ", ''.join(str(i) for i in data)
			break
		print "-------------------"
		time.sleep(0.5)