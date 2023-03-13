#!/usr/local/bin/python3.9

import sys
import json
from datetime import datetime

for jsonObj in sys.stdin:
    user = json.loads(jsonObj)
    print(datetime.strptime(user['yelping_since'], '%Y-%m-%d %H:%M:%S').month,':',1, sep='')
    
    
