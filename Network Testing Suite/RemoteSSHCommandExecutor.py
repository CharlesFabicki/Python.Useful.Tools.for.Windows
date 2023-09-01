import paramiko


def run_ssh_command(host, username, password, command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(host, username=username, password=password)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")

        if output:
            return f"Command output:\n{output}"
        elif error:
            return f"Command error:\n{error}"
        else:
            return "Command executed successfully."
    except paramiko.AuthenticationException:
        return "Authentication failed."
    except paramiko.SSHException as e:
        return f"SSH error: {e}"
    finally:
        ssh_client.close()


host = "example.com"
username = "your_username"
password = "your_password"
command = "ls -l"

result = run_ssh_command(host, username, password, command)
print(result)

# Here is a more advanced example of a python script that uses the paramiko library to automatically
# log into a remote server using ssh and execute commands on that server.
# This script can be used to manage remote servers or network devices: