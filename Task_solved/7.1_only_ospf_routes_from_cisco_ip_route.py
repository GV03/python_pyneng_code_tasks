#This Script is customized to take the show ip route cisco output as an input and filter out only OSPF routes and print it in
#expected_output template format.
#this can be customized based on the other requiremnet

file = open('only_ospf_route.txt', 'r')
line7 = file.readlines()
expected_output = '''
prefix          {}
AD/Metric       {}
Next-Hop        {}
Last Update     {}
Out Interface   {}'''

#print(line7[6:])
for line in line7[6:]:
    trimmed = line.replace("[","").replace("]","").replace(",","").split()
    if ("E2" or "E1" or "N1" or "N2" or "O") in trimmed:
        try:
            trimmed.remove("E2")
            trimmed.remove("O")
            trimmed.remove("E1")
            trimmed.remove("N1")
            trimmed.remove("N2")
        except ValueError:
            print(expected_output.format(trimmed[0],trimmed[1],trimmed[3],trimmed[4],trimmed[5]))


##output of this script is as below
#prefix          150.150.0.0
#AD/Metric       160/5
#Next-Hop        131.119.254.6
#Last Update     0:01:00
#Out Interface   Ethernet2
#
#prefix          192.68.132.0
#AD/Metric       160/5
#Next-Hop        131.119.254.6
#Last Update     0:00:59
#Out Interface   Ethernet2
#
#prefix          130.130.0.0
#AD/Metric       160/5
#Next-Hop        131.119.254.6
#Last Update     0:00:59
#Out Interface   Ethernet2

