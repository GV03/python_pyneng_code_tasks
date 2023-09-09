import textfsm
from tabulate import tabulate
from pymongo import MongoClient
import json
from pprint import pprint

traceroute = '''
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
'''
def trace_func():
  with open('traceroute.template') as template:
      template_contenet = textfsm.TextFSM(template)
      table_header = template_contenet.header
      parsed_data  = template_contenet.ParseText(traceroute)

  json_data = {}
  for hop, ip in parsed_data:
      json_data.update({hop:ip})

  return json_data
  #json_format = {}
  #for i,j in parsed_data:
  #    print(i)
  #    print(j)

  #print(parsed_data[0])
  #print(tabulate(parsed_data , headers= table_header))

if __name__ == '__main__':
   trace_func()