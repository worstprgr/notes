# Basic commands
Concatenate two or more files into one  
`cat txt_file_1 txt_file_2 txt_file_3 > new_text_file`  

Transfer a file to a remote Linux server. Make sure the user has permissions for that target directory  
`scp your_file_local user@server.com:/your_remote_path/your_file_name_on_remote`  

Add a new user, with a home directory  
`useradd -m <user name>`  

If you forgot the `-m` arg while creating a user, you can create the home directory for a specific user  
`mkhomedir_helper <user name>`  

Add a user to the sudoer file  
`usermod -aG sudo <user name>`  

Set the owner of a folder  
`sudo chown username: myfolder`  

Set the permissions of a folder for a user  
`sudo chmod u+w myfolder`  

**Modes**
| rwx  | r-x   | ---    |
|------|-------|--------|
| user | group | others |  

_Source:_ [Wikipedia - chmod](https://en.wikipedia.org/wiki/Chmod)  

