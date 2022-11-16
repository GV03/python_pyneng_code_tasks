##What Below scripts do?
##1. ask the user to enter the device name (r1, r2 or sw1),
# 1.1Print information about the corresponding device to standard output (information will be in the form of a dictionary).
##2.in addition to the device name, the script requested and then printed the device parameter as well.
##3.when requesting a parameter, a list of possible parameters was displayed. 
##3.1The list of parameters must be obtained from the dictionary, rather than written manually.
##4 when you request a parameter that is not in the device dictionary, the message ‘There is no such parameter’ is displayed
##5 when requesting a parameter, the user could enter the parameter name in any case.


london_co = {

    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
ask_device_name = input("Enter the Device name : ").lower()
list_of_device_elements = ", ".join((london_co[ask_device_name].keys()))
#print(list_of_device_elements)

ask_for_device_elements = input("Etner the device parameter ( {} ) : ".format(list_of_device_elements)).lower()
print("Below is the {1} detail of {0} you are looking for \n".format(ask_device_name,ask_for_device_elements))
print(london_co[ask_device_name].get(ask_for_device_elements,'No such parameter'))