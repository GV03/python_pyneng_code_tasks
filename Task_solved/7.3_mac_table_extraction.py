#this script will extract will go through the mac table of cisco command and extract corresponding entry of vlan,mac and interfaces and show it in ascending order based on the vlan value.
#also this ask to user about vlan number and and display only detali regarding that vlan id and mac address.

with open("cam_table.txt") as table:
    y = table.readlines()
    sorted_vlan = []
    for lines in y[6:]:
        words = lines.split()
        vlan,mac,type,intf = words
        sorted_vlan.append([int(vlan),mac,intf])

print(sorted_vlan)
for vlan,mac,intf in sorted(sorted_vlan):
    print("{:<10}{:<20}{}".format(vlan,mac,intf))

# -*- coding: utf-8 -*-

user_vlan = input("Enter VLAN number: ")

with open("cam_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit() and words[0] == user_vlan:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")
