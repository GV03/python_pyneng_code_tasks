import telnetlib
import time
from pprint import pprint


#below function convert bytes in unicode value.
def to_bytes(line):
    return f"{line}\n".encode("utf-8")

 
## below function return the command output value commands username, passwords and enable password is passed from main function
#
def send_show_command(ip, username, password, enable, commands):
    with telnetlib.Telnet(ip) as telnet:
        telnet.read_until(b"Username")
        telnet.write(to_bytes(username))
        telnet.read_until(b"Password")
        telnet.write(to_bytes(password))
        index, m, output = telnet.expect([b">", b"#"])
        if index == 0:
            telnet.write(b"enable\n")
            telnet.read_until(b"Password")
            telnet.write(to_bytes(enable))
            telnet.read_until(b"#", timeout=5)
        telnet.write(b"terminal length 0\n")
        telnet.read_until(b"#", timeout=5)
        time.sleep(3)
        telnet.read_very_eager()

        result = {}
        for command in commands:
            telnet.write(to_bytes(command))
            output = telnet.read_until(b"#", timeout=5).decode("utf-8")
            result[command] = output.replace("\r\n", "\n")
        return result

# below is the main function which defines the device iP to login and username and passrowds

if __name__ == "__main__":
    devices = [ "192.168.74.33", "192.168.74.44", "192.168.74.22", "192.168.74.146"]
    commands = ["sh ip int br", "sh arp"]
    for ip in devices:
        result = send_show_command(ip, "admin", "cisco", "cisco", commands)
        pprint(result, width=120)

