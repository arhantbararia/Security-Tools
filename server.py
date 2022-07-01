from yaml import MarkedYAMLError
from Server.connection import ServerConnection
from Server.handleConnection import handleConnection




SERVER_IP = "192.168.56.1"
SERVER_PORT = 8080


if __name__ == "__main__":
	my_socket = ServerConnection()
	print("socket created")
	my_socket.CreateConnection(SERVER_IP , 8080)
	print("socket binded with address")

	my_socket.Listen()
	print("socket listening for active connections")
	my_socket.AcceptConnection()
	

	handleConnection(my_socket)

