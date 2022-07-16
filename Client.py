
from Client.connection import clientConnection
from Client.handleConnection import handleConnection





if __name__ == "__main__":
   my_socket = clientConnection()

   my_socket.createConnection("192.168.56.1" , 8080)

   handleConnection(my_socket)
   print("Closing Connection")
   my_socket.close()

    


