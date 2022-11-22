#this script will go through the cisco configuration text file and will print only the lines without ! and any blank spaces and avoid configuration line from ignored list and save it to another file.


#config_file = open("cisco_switch_config.txt",'r')
#ignored_word = ["ip dhcp","control-plane","Current configuration"]
##print(config_file.readlines())
#for line in config_file.readlines():
#    if (line.startswith("!")):
#        line.strip("!")
#    elif line.startswith("\n"):
#        line.strip("")
#    else:
#        print(line.rstrip())


#with open('cisco_switch_config.txt') as f:
#   for line in f:
#       if not line.startswith("!"):
#           print(line.rstrip())

#config_file = open("cisco_switch_config.txt",'r')
ignored_word = ["ip dhcp","control-plane","Current configuration"]
#print(config_file.readlines())
with open("cisco_switch_config.txt") as src, open("dst_file.txt", 'w') as dst:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignored_word)
        if not line.startswith("!") and not words_intersect:
            dst.write(line)