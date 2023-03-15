import csv
from netmiko import ConnectHandler
import textfsm
from pprint import pprint
import json

target_version = "18.1(4)M7"

with open('C:/Users/gbvaghas/Desktop/device_version_check/device_inventory.csv','r') as inventory_file:
    inventory_reader = csv.DictReader(inventory_file)
    with open("upgrade_status.csv", "w", newline='') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['HostIP', 'Status', 'Comment'])
        for devices in inventory_reader:
            device_dict = { 
                "device_type": devices["Device_Type"],
                "ip": devices["Device_IP"],
                "username": devices["Device_Username"],
                "password": devices["Device_Password"],
            }
            #json_format = json.dumps(device_dict)
            #print(json_format)
            try :
                with ConnectHandler(**device_dict) as net_connect:
                    if device_dict["device_type"] == "cisco_ios":
                        output = net_connect.send_command("show version")
                        print(output)
            except :
                break
            