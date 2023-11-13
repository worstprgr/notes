# SSH: Login with Key
### Prerequisite
It's recommended, that you use an separate user to login, instead of `root`. After creating the key, proceed to turn of password logins entirely for all users.
In that way you minimize a attack vector.  

### On your client machine
1. Generate a new key `ssh-keygen -b 4096` with a passphrase
2. Transfer the key to the remote server: `ssh-copy-id -i ~/.ssh/key_rsa.pub name@yourserver.com`. *Note:* replace `key_rsa.pub` with the correct name of your public key
3. Test the connection with `ssh -i ~/.ssh/key_rsa name@yourserver.com` and login with your passphrase from the key

### On your server
*Turning off the password login and only allow a login with a SSH key*  

1. Open the sshd config file: `sudo nano /etc/ssh/sshd_config` and set the following items/values:
2. `PermitRootLogin prohibit-password`
3. `PubkeyAuthentication yes`
4. `ChallengeResponseAuthentication no`
5. `PasswordAuthentication no`
6. (systemd) restart the ssh service `sudo systemctl restart ssh`

### Source
> [Thomas-Krenn.com](https://www.thomas-krenn.com/de/wiki/OpenSSH_Public_Key_Authentifizierung_unter_Ubuntu) (German)

## SSH Config
Typing each time `ssh -i ~/.ssh/key_rsa name@yourserver.com` is kinda uncomfortable. So you can set up a configuration file instead.  
Inside `~/.ssh/` create a new file: `touch config` and edit it.  

```
Host <Your Alias>
    HostName <IP Adress or Domain>
    User <User name on the target server>
    IdentityFile <Path to the ssh key - usually: ~/.ssh/id_key>
```

Now you can access your server via SSH using this command: `ssh <Your Alias>`.  

### Storing SSH Passphrase (Optional)
If your SSH key has a passphrase (which it should have), you can store it to the key chain.  
That allows you to skip the password prompt, while accessing your server via SSH.  

1. Invoke the SSH-agent: ``eval `ssh-agent -s` ``
2. Add you keys to it: `ssh-add ~/.ssh/id_key`

Regarding this [source](https://www.oreilly.com/library/view/linux-security-cookbook/0596003919/ch06s11.html), 
it is recommended to shut down the SSH-agent at every logout. You can add in your `~/.logout` file a entry: `kill $SSH_AGENT_PID`.  
The exact name of the `.logout` file depends on your shell. If you're using bash, so it's `.bash_logout`.

