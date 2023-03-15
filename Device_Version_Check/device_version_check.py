import csv
from netmiko import ConnectHandler
import textfsm

# Target software version
target_version = "18.1(4)M7"


# Open inventory file and read device details
with open('C:/Users/gbvaghas/Desktop/device_version_check/device_inventory.csv','r') as inventory_file:
    inventory_reader = csv.DictReader(inventory_file)
    # Create output CSV file
    with open("upgrade_status.csv", "w", newline="") as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(["Host", "Status", "Comment"])
        # Iterate through devices
        for device in inventory_reader:
            # Create device dictionary for Netmiko
            device_dict = {
                "device_type": device["Device_Type"],
                "ip": device["Device_IP"],
                "username": device["Device_Username"],
                "password": device["Device_Password"],
            }
            # Try to connect to the device
            try:
                with ConnectHandler(**device_dict) as net_connect:
                    # Determine device vendor
                    if device_dict["device_type"] == "cisco_ios":
                        # Get show version output and parse with TextFSM
                        output = net_connect.send_command("show version")
                        with open("cisco_ios_show_version_template.textfsm") as template_file:
                            template = textfsm.TextFSM(template_file)
                            fsm_results = template.ParseText(output)
                            # Extract software version
                            software_version = fsm_results[0][10]
                    elif device_dict["device_type"] == "juniper_junos":
                        # Get show version output and parse with TextFSM
                        output = net_connect.send_command("show version | no-more")
                        with open("juniper_junos_show_version_template.textfsm") as template_file:
                            template = textfsm.TextFSM(template_file)
                            fsm_results = template.ParseText(output)
                            # Extract software version
                            software_version = fsm_results[0][4]
                    else:
                        # Unsupported device type
                        output_writer.writerow([device_dict["ip"], "Failed", "Unsupported device type"])
                        continue
                    # Compare software version with target version
                    if software_version < target_version:
                        output_writer.writerow([device_dict["ip"], "Upgrade needed", f"Fetched version: {software_version}"])
                    else:
                        output_writer.writerow([device_dict["ip"], "No upgrade needed", f"Fetched version: {software_version}"])
            except Exception as e:
                # Connection failed
                output_writer.writerow([device_dict["ip"], "Failed", f"{type(e).__name__}: {str(e)}"])
                continue
