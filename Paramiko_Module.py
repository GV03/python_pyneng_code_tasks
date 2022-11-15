#Paramiko provides client-server functionality and it is implementation of SSHv2 in python
#Below covers the client functionality of the paramiko 


import paramiko
import time
import socket
from pprint import pprint

#sh_client = paramiko.SSHClient() #client is created, this class represent connection to SSH server
#
#Client configuraiton is set
#sh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#sh_client.connect(hostname="192.168.74.44", username='admin',password='cisco',look_for_keys=False,allow_agent=False )
#
#pen_ssh_connection = ssh_client.invoke_shell()
#
#pen_ssh_connection.send("enable\n")
#ime.sleep(2)
#pen_ssh_connection.send("cisco\n")
#ime.sleep(2)
#pen_ssh_connection.send("show ip interf br\n")
#ime.sleep(2)
#output = open_ssh_connection.recv(5000)
#open_ssh_connection.close()
#print(output)


import paramiko
import time
import socket
from pprint import pprint


def send_show_command(
    ip,
    username,
    password,
    enable,
    command,
    max_bytes=60000,
    short_pause=1,
    long_pause=5,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.send("enable\n")
        ssh.send(f"{enable}\n")
        time.sleep(short_pause)
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        ssh.recv(max_bytes)

        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(5)

            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result[command] = output

        return result


if __name__ == "__main__":
    devices = [ "192.168.74.33", "192.168.74.44", "192.168.74.22", "192.168.74.146"]
    commands = ["sh clock", "sh arp"]
    for ip in devices:
        result = send_show_command(ip, "admin", "cisco", "cisco", commands)
        pprint(result, width=120)
