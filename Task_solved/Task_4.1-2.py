
#Task 4.1
#Using the prepared nat string, get a new string where the FastEthernet interface is replaced with GigabitEthernet. 
#Print the resulting new string to the standard output (stdout) using print.
#nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

old_nat_statment = "ip nat inside source list ACL interface FastEthernet0/1 overload"

new_nat_statment = old_nat_statment.replace('Fast','Gigabit')
print(new_nat_statment) #changed from FastEthernet0/1 to GigabitEthernet0/1 and print

#Task 4.2
#Convert string in mac variable from XXXX:XXXX:XXXX format to XXXX.XXXX.XXXX format. 
#Print the resulting new string to the standard output (stdout) using print.
#mac = "AAAA:BBBB:CCCC"

old_mac_format = "AAAA:BBBB:CCCC"
new_mac_format = old_mac_format.replace(':','.')
print (new_mac_format)
