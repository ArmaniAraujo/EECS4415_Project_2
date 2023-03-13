#!/usr/local/bin/python3.9

import sys

dataDict = {}

for line in sys.stdin:
    id, date, ufc = line.strip().split('\t')
    dataDict[(id,date)] = ufc

# https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
sortedDataList = sorted(dataDict.items(), key=lambda x:x[1], reverse=True)

for item in range(0,4415):
    print(sortedDataList[item][0][0], sortedDataList[item][1], sep='\t')


    