
import socket


SERVER_IP = "192.168.56.1"
SERVER_PORT = 8080


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    address = (SERVER_IP, SERVER_PORT)
    sock.connect(address)
    
    msg_recieved = sock.recv(1024);
    
    print(msg_recieved.decode())
    
    sock.close();