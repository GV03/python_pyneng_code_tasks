#extract the IP address while user input with mask and convert IP address in binary format


ask_ip_network = input('Enter ip network address with mask : ') #e.g = 192.168.0.0/24
ip_list1 = ask_ip_network.split('.')
mask_extract = ip_list1.pop(-1)
mask_extract = mask_extract.split('/')
#print(mask_extract)
ip_list1.append(mask_extract[0])
#print(ip_list1)
Network_output = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(Network_output.format(int(ip_list1[0]),int(ip_list1[1]),int(ip_list1[2]),int(ip_list1[3])))


###Example output#############
#Network:
#192       168       45        23
#11000000  10101000  00101101  00010111
