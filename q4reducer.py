#!/usr/local/bin/python3.9

import sys
import uuid
import random

uidSet = set({})

def uidGenerator():
    global uidSet
    a = uuid.uuid1()
    while True:
        if a not in uidSet:
            a = str(a)[:22]
            a = str(a).replace('-', '_')
            randomIndex = random.randint(0,21)
            temp = list(a)
            temp[randomIndex] = temp[randomIndex].upper()
            a = ''.join(temp)
            uidSet.add(a)
            return a
        else:
            a = uuid.uuid1()

for line in sys.stdin:
    business_id, business_name, timestamp = line.strip().split('\t')
    print(uidGenerator(), timestamp, business_name, sep='\t', end='\n')

