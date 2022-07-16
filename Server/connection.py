from curses.ascii import DEL
import socket
import zipfile

DELIMITER = "<EOF>"

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
    
    def upload_file(self, file_path):

        with open(file_path , 'rb') as file:
            chunk = file.read(4096)

            while( len(chunk) > 0 ):
                self.client_sock.send(chunk)

                chunk = file.read(4096)

            self.client_sock.send(DELIMITER.encode())

            print("Transfer complete")

    def download_file(self):
        print("navigate to the path and ")
        path = input("Enter path >> ")
        self.send_data(path)

        print("waiting for the files...")

        filename  = self.recieve_data()
        print("Downloading " , filename)

        with open(filename , "wb") as file:
            while True:
                chunk = self.client_sock.recv(4096)

                if chunk.endswith(DELIMITER.encode()):
                    chunk = chunk[: -len(DELIMITER)]
                    file.write(chunk)
                    break

                file.write(chunk)
            print("[+] Transfer complete")
            



