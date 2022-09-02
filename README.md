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

![Untitled 1](https://user-images.githubusercontent.com/61796574/188238140-d24ec980-630b-4c09-8d62-d0a8ba6d7d68.png)

When you run the program, the CLI provided is pretty self-explanatory.
Here, I have used an Ubuntu machine to run as server. And my target machine is a Windows machine.

### 1. Running commands

![Untitled 2](https://user-images.githubusercontent.com/61796574/188238210-140e38c0-0bd0-4b87-b1bb-77e2236e5497.png)

The current working directory of client machine is visible. And an option after “>>” to run the commands.

Here, I try to run “””systeminfo””” which is a Windows PowerShell command for printing out the system information. And as expectedly it worked and as can be seen in image client machine is running a version of windows. 

### 2. Upload file to client machine.

![Untitled](https://user-images.githubusercontent.com/61796574/188238241-034ace4e-a99e-4b39-9063-1b0de6b8f9f9.png)

After entering the path to the file which is to be uploaded to client. It can be seen that the file “poster_event.pdf” is present in the current working directory of the client.

### 3. Downloading File from client machine

This function is experiencing some issues as of right now. I am working on it.

### 4. Capturing state of the client.

This function is experiencing some issues as of right now. I am working on it.

## To Do

- [ ]  Repair file transfer from Client to Server.
- [ ]  Reduce complexities
- [ ]  Add installation guide to README
