from datetime import datetime
import time
from detectqr import *
import json

import cozmo
import http.client
import asyncio

def after_cap(robot: cozmo.robot.Robot):
    b = decodeQR()
    if len(b) == 0:
        robot.say_text("Can not detect any qr code" + " " + "please try again").wait_for_completed()
    b = json.loads(b.decode("utf-8").replace("'",'"'))
    print(b)
    # b = {'medname': 'Aspirin', 
    #       'quantity': '1', 
    #       'total': '10', 
    #       'time': ['12:00', '20:30']
    #       }
    breakfast_start = "07:30"
    breakfast_end = "10:00"

    lunch_start = "12:00"
    lunch_end = "14:00"

    dinner_start = "17:30"
    dinner_end = "20:30"

    for i in range(len(b['time'])):
        if b['time'][i] < dinner_start and b['time'][i] < lunch_start :\
            b['time'][i] = "breakfast"
        elif b['time'][i] > breakfast_end and b['time'][i] < dinner_end :
            b['time'][i] = "lunch"
        else :
            b['time'][i] = "dinner"

    robot.say_text(" This medicine name " + '     ' + b['medname']  + ' ' + ' ' + " You have to take on").wait_for_completed()
    for j in b['time']:
        robot.say_text(j).wait_for_completed()
    
    robot.say_text("for" + ' ' + b['quantity'] + ' ' + " tablets " + ' ' + 'in each times').wait_for_completed()