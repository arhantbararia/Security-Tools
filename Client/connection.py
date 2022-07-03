from ctypes import addressof
import socket
import os
import zipfile


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
    
    def download_file(self):
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

    def upload_file(self , path):
        filename = os.path.basename(path).split(".")[0]

        zipped_name = filename + '.zip'

        zipf = zipfile.ZipFile(zipped_name , "w" )
                                                                                        #zipping the file
        if os.path.isdir(path):
            for root , dirs , files in os.walk(path):
                for file in files:
                    zipf.write(os.path.join(root , file))
            zipf.close()
        else:
            zipf.write(path)

        with zipfile.ZipFile(zipped_name , "r") as zip:
                zip.printdir()
            
        self.send_data(zipped_name)
        with open(zipped_name , 'rb') as file:
            chunk = file.read(4096)

            while( len(chunk) > 0 ):
                self.socket.send(chunk)

                chunk = file.read(4096)

            self.socket.send(DELIMITER.encode())

            print("Transfer complete")
        

        




    def close(self):
        self.socket.close()
    
