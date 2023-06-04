import socket

#set ports
ports = []

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.2)
	#set target
	code = client.connect_ex(("", port))
	if code == 0:
		print (port, "aberta.")
