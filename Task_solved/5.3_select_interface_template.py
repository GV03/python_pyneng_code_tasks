##This Script will select the interface template based on the mode of the interface either trunk or access.
##also will ask two different question of single vlan and list of vlan based on the mode of interface selected.
###Versuon 1 of the script

access_template = """
switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""

interface_template = {"access": access_template, "trunk":trunk_template}
question = {"access": "Enter VLAN number: ", "trunk": "Enter the allowed VLANs: "}

interface_mode = input("Enter interface mode (access/trunk) : ")
interface_number = input("Enter the type of interface and number : ")
interface_vlan = input(question[interface_mode])###this used to give list of vlan or only single vlan number based on the mode of the interfaces slected

print("Below is the template for {} if used in {} mode".format(interface_number,interface_mode))
print("interface {}".format(interface_number.rstrip()))
print(interface_template[interface_mode].format(interface_vlan))



##Below script is next version of previouse interface script
#this script will add/remove/single vlans based on trunk interfaces action given in interface and vlan dictniory 
##this script uses hardcorded value in script not user specific value, we can ask user for input instead of static entry in script.
##Version2



access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

##for access mode interface template
for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

 ##for trunk mode interface template 
for intf, vlan in trunk.items():
    print("interface FastEthernet{}".format(intf))
    for command in trunk_template:
        if command.endswith("allowed vlan") and ("add" in vlan ):
            print(command + " " + vlan[0] + " " + ",".join(vlan[1:]))
        elif (command.endswith("allowed vlan") and ("only" in vlan)):
            print(command + " " + vlan[0].replace("only","") + " " + ",".join(vlan[1:]))
        elif (command.endswith("allowed vlan") and ("del" in vlan)):
            print(command + " " + vlan[0].replace("del","remove") + " " + ",".join(vlan[1:]))
        else:
            print(command)

