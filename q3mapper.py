#!/usr/local/bin/python3.9

import json
import sys

output = ''

for jsonObj in sys.stdin:
    tempObj = json.loads(jsonObj)
    ufc = int(tempObj['useful']) + int(tempObj['funny']) + int(tempObj['cool'])
    print(tempObj['review_id'], '\t', tempObj['date'], '\t', ufc, sep='')
