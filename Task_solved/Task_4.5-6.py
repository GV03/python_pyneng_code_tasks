#Task 4.5
#From the strings command1 and command2, 
# get a list of VLANs that exist in both command1 and command2 (intersection)
#In this case, the result should be a list: ['1', '3', '8'].
#Print the resulting list to the standard output (stdout) using print.

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

new_command1_vlan = command1.split()[-1].split(',')
new_command2_vlan = command2.split()[-1].split(',')

#print(new_command1_vlan)
#print(new_command2_vlan)

common_vlans_in_command = sorted((set(set(new_command1_vlan).intersection(set(new_command2_vlan)))))
#print(common_vlans_in_command)

#########################################################################################
#Task 4.6
#Process the ospf_route string and print the information to the stdout as follows:
#ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route =  "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
removed_space = ospf_route.strip()
#print(removed_space)
removed_space = removed_space.replace("[","").replace("]","").replace(",","")
list_of_element = removed_space.split()
print(list_of_element)
print("Prefix\t\t{}".format(list_of_element[0]))
print("AD/Metric\t\t{}".format(list_of_element[1]))
print("Next-Hop\t\t{}".format(list_of_element[3]))
print("Last update\t\t{}".format(list_of_element[4]))
print("Outbound Interface\t\t{}".format(list_of_element[5]))



################other solution of 4.6 as below###########

#ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
#template = """
#Prefix                {}
#AD/Metric             {}
#Next-Hop              {}
#Last update           {}
#Outbound Interface    {}
#"""
#route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
#route = route.split()
#
#print(template.format(route[0], route[1], route[3], route[4], route[5]))







