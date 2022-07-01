import socket

class ServerConnection:
    def __init__(self):
        #Creates a socket for server to listen to
        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    def CreateConnection(self , ip = "" , port = 8080):
        self.address = (ip, port);
        self.socket.bind(self.address)

    def Listen(self , backlog = 5):
        self.socket.listen(backlog)

    def AcceptConnection(self):
        self.client_sock , self.client_add = self.socket.accept()     ##recieves client socket(bridge) and address(with port)
        print("[+] Connection Established ", self.client_add)

        return self.client_sock , self.client_add
    
    def send_data(self, userinput):
        sendData = bytes(userinput, "UTF-8")
        self.client_sock.send(sendData)

    
    def recieve_data(self):
        rcdData = self.client_sock.recv(8*1024)
        rcdData = rcdData.decode("UTF-8")
        return rcdData
    
        