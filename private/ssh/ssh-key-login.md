# SSH: Login with Key
### Prerequisite
It's recommended, that you use an separate user to login, instead of `root`. After creating the key, proceed to turn of password logins entirely for all users.
In that way you minimize a attack vector.  

### On your client machine
1. Generate a new key `ssh-keygen -b 4096` with a passphrase
2. Transfer the key to the remote server: `ssh-copy-id -i ~/.ssh/key_rsa.pub name@yourserver.com`. *Note:* replace `key_rsa.pub` with the correct name of your public key
3. Test the connection with `ssh -i ~/.ssh/key_rsa.pub name@yourserver.com` and login with your passphrase from the key

### On your server
*Turning off the password login and only allow a login with a SSH key*  

1. Open the sshd config file: `sudo nano /etc/ssh/sshd_config` and set the following items/values:
2. `PermitRootLogin prohibit-password`
3. `PubkeyAuthentication yes`
4. `ChallengeResponseAuthentication no`
5. `PasswordAuthentication no`
6. (systemd) restart the ssh service `sudo systemctl restart ssh`

### Source
- [Thomas-Krenn.com](https://www.thomas-krenn.com/de/wiki/OpenSSH_Public_Key_Authentifizierung_unter_Ubuntu) (German)
