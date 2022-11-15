#Task4.7
#Convert MAC address in mac string to binary string like this:
#101010101010101010111011101110111100110011001100

mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','')
print(mac)
bin_mac = "{:b}".format(int(mac,16))
print(bin_mac)


#Task4.8
#Convert the IP address in the ip variable to binary and print output in columns to stdout:
#the first line must be decimal values
#the second line is binary values
#Example output for address 10.1.1.1:
#10        1         1         1
#00001010  00000001  00000001  00000001

ip = "192.168.3.1"
ip = ip.split(".")
output = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}""".format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))

print(output)
