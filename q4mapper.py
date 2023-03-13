#!/usr/local/bin/python3.9

import json
import sys

businessDataset = {}
checkInDataset = {}

for jsonObj in sys.stdin:
    line = json.loads(jsonObj)

    if 'name' in line:          # implies that the line read is from business dataset
        businessDataset[line['business_id']] = line['name']
    else:                       # Otherwise is from checkin dataset
        business_id = line['business_id']
        timestamps = line['date'].split(', ')
        checkInDataset[business_id] = timestamps

for key in businessDataset.keys():
    if key in checkInDataset.keys():
        for items in checkInDataset[key]:
            print(key, businessDataset[key], items, sep='\t', end='\n')


