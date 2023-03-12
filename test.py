import json

businessList = []

with open('yelp_academic_dataset_business.json', encoding='utf-8') as f:
    for jsonObj in f:
        tempObj = json.loads(jsonObj)
        businessList.append(tempObj)

        if(businessList[-1]['hours'] is not None) :
            if('Saturday' in businessList[-1]['hours'] or 'Sunday' in businessList[-1]['hours']):
                print('in')
            else: print('out')