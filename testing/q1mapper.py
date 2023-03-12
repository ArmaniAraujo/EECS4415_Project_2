#!/usr/local/bin/python3.9

'''
    any business. not just restaurant
    hours --> saturday:time/sunday:time
'''

import sys
import json

businessList = []

for jsonObj in sys.stdin:
    tempObj = json.loads(jsonObj)
    businessList.append(tempObj)
    
    # check if there categories are listed
    # and if hours are listed
    # if yes, check if they are open on either Sat/Sun or both
    if (businessList[-1]['categories'] is not None and businessList[-1]['hours'] is not None) :
            if('Saturday' in businessList[-1]['hours'] or 'Sunday' in businessList[-1]['hours']):
                categoryList = businessList[-1]['categories'].split(', ')
                businessID = businessList[-1]['business_id']
                for category in categoryList:
                  print(category,':',businessID, sep='')

    # with open('q1mapper.out', 'a') as w:
    #     for category in categoryList:
    #         w.write(category + ':' + businessList[-1]['business_id'] + '\n')

    
    categoryList.clear()


