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
    if (category in dataDict):
        dataDict[category].append('\'' + business + '\'')
    else:
        dataDict[category] = list(['\'' + business + '\''])

for cat in dataDict:
    output = cat + ' \t[' + ', '.join(dataDict[cat]) + ']'
    print(output)


