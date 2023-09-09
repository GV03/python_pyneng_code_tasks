import json
from pprint import pprint
import parsing

with open('student.json') as f:
  data = json.load(f)

pprint(data)


