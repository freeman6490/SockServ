#!/usr/bin/python3
import socket
#simple server app

#create socket object
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind it to somewhere
listener.bind(("", 8080)) #empty string means you can connect to any IP
#starts listening
listener.listen(1)

while True:
#accept a connection
	sock, addr = listener.accept()

	#give some info about it
	print("View connection from", addr)
	#send a prompt
	sock.send(b"Tell me your name")
	name = sock.recv(512)
	name = str(name).strip()
	#send them something
	sock.send(b"Welcome to my server" + (bytes(name, "ASCII") +b".\nGoodbye"))
	sock.close()

listener.close()
