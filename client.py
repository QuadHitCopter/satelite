import socket
from time import sleep
from datetime import datetime
import os
import json
def clear():
	os.system("clear")


host = 'local host'
port = 5000
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)


s.connect(('192.168.0.12', port))
receive = s.recv(1024)
print("Conexión establecida \n")
sleep(2)
clear()
com_t = 0
received = False
while receive and com_t!="end":
	clear()
	if received:
		print("RASPBERRY-HAISE  Comando recibido:", com_dic)
	receive = s.recv(1024)
	time = str(datetime.now())
	com_t = receive.decode()
	if com_t != "end":
		com_dic= {
			"command":com_t,
			"rec_date":time,
			"state":None
	}
		com_json = json.dumps(com_dic,indent = 1)

		with open("coms.json","w") as updating:
			updating.write(com_json)
		#print("saved:",com_dic)
		received = True
	sleep(0.02)


s.close()
