from ctypes import addressof
import socket

DELIMITER = "<EOF>"
class clientConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    def createConnection(self, ip = "" , port = 8080):
        self.address = (ip , port)
        self.socket.connect(self.address)

    def send_data(self, userInput):
        sendData = bytes(userInput, "UTF-8")
        self.socket.send(sendData)

    def recieve_data(self):
        recd = self.socket.recv(8*1024)
        self.data = recd.decode("UTF-8")
        return self.data
    
    def recieve_file(self):
        filename = self.recieve_data()
        print("Downloading: " , filename)
        with open(filename , "wb") as file:
            while True:
                chunk = self.socket.recv(4096)

                if chunk.endswith(DELIMITER.encode()):
                    chunk = chunk[: -len(DELIMITER)]
                    file.write(chunk)
                    break

                file.write(chunk)
            print("[+] Transfer completed")



    def close(self):
        self.socket.close()
    
