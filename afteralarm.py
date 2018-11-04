from datetime import datetime
import time
from detectqr import *
import json
import cozmo

def after_alarm(robot: cozmo.robot.Robot):
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
        #cozmosay
        print("YES")
        robot.say_text("Hey! DEAR it's time to take medicine!").wait_for_completed()

    else :
        #line notify
        print("NO")
    
