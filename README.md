# Remote Access Tool

Version 1.0

## About

Get remote access to the terminal of the client machine.

- Access to terminal
- Upload file
- download file
- Explore the client machine.
- Capture client machine state.

For now, it supports only Windows machines as the clients, and any machine (Windows/Mac/Linux) can be used to play as server.

![Untitled](Remote%20Access%20Tool%203efe9d508fc04478894b5c9881d6ab59/Untitled.png)

When you run the program, the CLI provided is pretty self-explanatory.
Here, I have used an Ubuntu machine to run as server. And my target machine is a Windows machine.

### 1. Running commands

![Untitled](Remote%20Access%20Tool%203efe9d508fc04478894b5c9881d6ab59/Untitled%201.png)

The current working directory of client machine is visible. And an option after “>>” to run the commands.

Here, I try to run “””systeminfo””” which is a Windows PowerShell command for printing out the system information. And as expectedly it worked and as can be seen in image client machine is running a version of windows. 

### 2. Upload file to client machine.

![Untitled](Remote%20Access%20Tool%203efe9d508fc04478894b5c9881d6ab59/Untitled%202.png)

After entering the path to the file which is to be uploaded to client. It can be seen that the file “poster_event.pdf” is present in the current working directory of the client.

### 3. Downloading File from client machine

This function is experiencing some issues as of right now. I am working on it.

### 4. Capturing state of the client.

This function is experiencing some issues as of right now. I am working on it.

## To Do

- [ ]  Repair file transfer from Client to Server.
- [ ]  Reduce complexities
- [ ]  Add installation guide to README
