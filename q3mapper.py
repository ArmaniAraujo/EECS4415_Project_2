#!/usr/local/bin/python3.9

import json

counter = 0
output = ''

with open('yelp_academic_dataset_review.json', encoding='utf-8') as f:

    for jsonObj in f:
        tempObj = json.loads(jsonObj)
        ufc = int(tempObj['useful']) + int(tempObj['funny']) + int(tempObj['cool'])
        print(tempObj['review_id'], '\t', ufc, '\t', tempObj['date'], sep='')



