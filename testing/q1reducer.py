#!/usr/local/bin/python3.9

import sys

'''   
    TODO:   Currently working with unsorted file
            Should I sort it? If so, where? who does the sorting?
    TODO:   Possibly need to output final information onto console instead
'''

dataDict = {}

for line in sys.stdin:
    category, business = line.strip().split(':')
    print(category, business)
    if (category in dataDict):
        dataDict[category].append('\'' + business + '\'')
    else:
        dataDict[category] = list(['\'' + business + '\''])

for cat in dataDict:
    output = cat + ' \t[' + ', '.join(dataDict[cat]) + ']'
    print(output)
# with open('q1reducer.out', 'w') as w:
#     for cat in dataDict:
#         w.write(cat + ' \t[')
#         w.write(', '.join(dataDict[cat]))
#         w.write(']\n')
#print(output)
