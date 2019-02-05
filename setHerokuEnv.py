import json
import os
from pprint import pprint
import sys
with open('findtheroommate-firebase-adminsdk-b2xem-031d66f91d.json') as json_data:
    vars = json.load(json_data)
pprint(vars)

# https://stackoverflow.com/questions/89228/calling-an-external-command-in-python

addl_args = ""
for a in sys.argv[1:]:
    addl_args += (" " + a)

for k in vars.keys():
    command = "heroku config:set " + k + "=" + vars[k] + addl_args;
    print("executing: " + command);
    os.system(command);
