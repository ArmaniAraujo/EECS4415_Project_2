#!/usr/local/bin/python3.9

import sys
import json

dataDict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0,
            7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
total = 0

for line in sys.stdin:
    month, count = line.strip().split(':')
    total += 1
    if (month in dataDict):
        dataDict[month] += 1
    else:
        dataDict[month] = 1

for month in dataDict:
    print(month, '\t', round(dataDict[month]/total * 100, 2), '%', sep='')