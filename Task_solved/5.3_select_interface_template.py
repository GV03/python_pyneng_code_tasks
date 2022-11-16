##This Script will select the interface template based on the mode of the interface either trunk or access.
##also will ask two different question of single vlan and list of vlan based on the mode of interface selected.


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




