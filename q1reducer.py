#!/usr/local/bin/python3.9

dataDict = {}

'''   
    TODO:   Currently working with unsorted file
            Should I sort it? If so, where? who does the sorting?
    TODO:   Possibly need to output final information onto console instead
'''

with open('q1mapper.out', encoding='utf-8') as f:
    for line in f:
        category, business = line.strip().split(':')

        if (category in dataDict):
            dataDict[category].append('\'' + business + '\'')
        else:
            dataDict[category] = list(['\'' + business + '\''])

with open('q1reducer.out', 'w') as w:
    for cat in dataDict:
        w.write(cat + ' \t[')
        w.write(', '.join(dataDict[cat]))
        w.write(']\n')

