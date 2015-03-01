
# SSH Keys

To increase security, you can disable password logins and rely on ssh public keys. To do
this, take a look [here](https://wiki.archlinux.org/index.php/SSH_Keys) for details. Basic
steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA (1024 bit) both 
public and private keys. They will be stored in `~/.ssh` with the public key having .pub 
appended to the end.

        ssh-keygen -t dsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"
    
    Note you can create a key for a different username if you change $(whoami) to the user name you want.

2. Copy the public key (.pub) to the server you will connect to:

        ssh-copy-id username@remote-server.org 

    This should update ~/.ssh/authorized_keys in the process. Also ensure the correct 
protections are on the file by:

        chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/ssh/sshd_config to disable password logins.

		PasswordAuthentication no
		ChallengeResponseAuthentication no

    
