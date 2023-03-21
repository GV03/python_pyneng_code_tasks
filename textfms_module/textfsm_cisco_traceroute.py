import textfsm

traceroute_output = '''
R1#traceroute 8.8.8.8

Type escape sequence to abort.
Tracing the route to dns.google [8.8.8.8]

  1  192.168.1.1  1 msec  1 msec  1 msec
  2  10.10.10.1  4 msec  4 msec  3 msec
  3  172.16.10.1  8 msec  9 msec  8 msec
  4  200.10.10.1  11 msec  12 msec  13 msec
  5  201.20.20.1  18 msec  19 msec  18 msec
  6  205.30.30.1  28 msec  30 msec  27 msec
  7  207.40.40.1  33 msec  35 msec  32 msec
  8  208.50.50.1  42 msec  44 msec  42 msec
  9  209.60.60.1  49 msec  50 msec  49 msec
 10  8.8.8.8  52 msec  54 msec  52 msec

'''
with open('C:/Users/gbvaghas/OneDrive - Nokia/Module_Textfsm/traceroute.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute_output)

print(fsm.header)
for i in range(len(result)):
    print(result[i])
