import csv
import os
from netmiko import ConnectHandler

# Set the target software version
target_version = "13.1(4)M8"

with open('C:/Users/gbvaghas/Desktop/device_inventory.csv','r') as datafile :
    readcsv = csv.DictReader(datafile)
    for row in readcsv:
        ip_address = row['Device_IP']
        device_type = row['Device_Type']
        username = row['Device_Username']
        password = row['Device_Password']
        try: 
            device = ConnectHandler(device_type=device_type, ip='192.168.74.11', username='admin', password='cisco')
            output = device.send_command('show version')
#print (output)
            device.disconnect()
            if "Cisco IOS Software" in output:
                version = output.split('Version ')[1].split(",")[0]
                print(ip_address, version)
            if version < target_version:
                status = "Upgraded needed"
            else:
                status = "No upgrade needed"
            print(status)



            