#!/usr/local/bin/python3.9

'''
    any business. not just restaurant
    hours --> saturday:time/sunday:time

    TODO:   Try to put outputString into string variable
            and print entire thing into file later
'''

import json
import os

# Deletes the q1mapper file if it exists
if os.path.exists("q1mapper.out"):
  os.remove("q1mapper.out")
else:
  print("The file does not exist")

businessList = []
outputStr = ''

print("reading...")
with open('yelp_academic_dataset_business.json', encoding='utf-8') as f:
    for jsonObj in f:
        tempObj = json.loads(jsonObj)
        businessList.append(tempObj)
        
        # check if there categories are listed
        # and if hours are listed
        # if yes, check if they are open on either Sat/Sun or both
        if (businessList[-1]['categories'] is not None and businessList[-1]['hours'] is not None) :
                if('Saturday' in businessList[-1]['hours'] or 'Sunday' in businessList[-1]['hours']):
                    categoryList = businessList[-1]['categories'].split(', ')

        with open('q1mapper.out', 'a') as w:
            for category in categoryList:
                w.write(category + ':' + businessList[-1]['business_id'] + '\n')

        categoryList.clear()

print('completed')



