import socket
from time import sleep
from datetime import datetime
import os
import pickle

def clear():
	os.system("clear")


host = 'local host'
port = 4000
d = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)


d.connect(('192.168.0.12', port))
name = str(datetime.now())[0:-6]
d.send(b"name")

end = False
n = 0
while end !=True:
	n+=1
	time = str(datetime.now()) + " OK"



	if n< 40:
		dic = {"time":time,"state":"Normal","v5":5}
		coded_dic = pickle.dumps(dic)
		print(coded_dic)
		d.send(coded_dic)
		sleep(0.2)
	else:
		d.send(b"end")
		end = True



d.close()
