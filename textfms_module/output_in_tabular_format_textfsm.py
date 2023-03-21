import textfsm
import sys
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    template_read = textfsm.TextFSM(f)
    parse_result = template_read.ParseText(output.read())
    header = template_read.header
    #print(parse_result)
    print(tabulate(parse_result, headers = header))

##This script will ask for 2 input while running..
#1st place template name and 2nd name text file name
# this place give output in tabular format after extracting information from text file 
#example below

#PS C:\Users\gbvaghas\OneDrive - Nokia\Module_Textfsm> python .\output_in_tabular_format_textfsm.py .\showclock.template .\cisco_show_clock.txt        
#Time      Timezone    WeekDay    Month      MonthDay    Year
#--------  ----------  ---------  -------  ----------  ------
#13:30:55  UTC         Sun        Mar              21    2023