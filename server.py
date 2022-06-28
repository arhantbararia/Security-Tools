import socket

SERVER_IP = "192.168.56.1"
SERVER_PORT = 8080


if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	address = (SERVER_IP , SERVER_PORT)
	sock.bind(address)
	
	sock.listen(1)	

	print("[+] Waiting for incomming connection: ", SERVER_PORT)
	client_sock, client_add = sock.accept()
	print("[+] Connection Established:", client_add)
	
	msg = "This is Response from server"
	client_sock.send(msg.encode())
	

	client_sock.close()
