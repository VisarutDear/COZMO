from datetime import datetime
import time
from detectqr import *
import json
import datetime
import math
import sys
import time
import asyncio
import cozmo


a = decodeQR()
a = json.loads(a.decode("utf-8").replace("'",'"'))
print(a['time'])
print(a)
alarm_time = ["breakfast","lunch","dinner","bed"]

alarm_med = []
breakfast = a['time']
lunch = "12:00"
dinner = "17:00"
bed = "20:30"
#now = datetime.now().strftime("%H:%M")
if breakfast == '08.00' :
    print("YES")
else :
    print("NO")
    
