#this script change the mac address format from non-cisco supported format to cisco supported format


mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
cisco_mac_format = []
for mac_index in range(len(mac)):
    #print(old_mac_format)
    cisco_mac_format.append(mac[mac_index].replace(':','.'))
print(cisco_mac_format)signal