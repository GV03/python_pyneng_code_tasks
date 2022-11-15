#Task 4.3
#Get the following list of VLANs from the config string: ["1", "3", "10", "20", "30", "100"]
#Write the resulting list to the result variable. (this is the variable that will be checked in the test)
#Print the resulting list to the standard output (stdout) using print.
#Here is a very important point that you need to get exactly the list (data type), and not, for example, a string that looks like the list shown.
#config = "switchport trunk allowed vlan 1,3,10,20,30,100"

config_line = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlan_index = config_line.split()[-1].split(',') #take the string and split it so that will get VLAN's index and it's content in string format and then again split it with , and will get list of vlan list
#print(vlan_index)


#Task 4.4
#remove duplicate vlans from the list and and sort it in ascending order of number and print
#vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
non_duplicate_vlan_list = set(vlans)
#print(non_duplicate_vlan_list)
sorted_vlan_list = list(sorted(non_duplicate_vlan_list))
print(sorted_vlan_list)
