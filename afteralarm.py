from datetime import datetime
import time
from detectqr import *
import json
import cozmo
import http.client

def after_alarm(robot: cozmo.robot.Robot):
    a = decodeQR()
    a = json.loads(a.decode("utf-8").replace("'",'"'))
    print(a)
    # a = {'owner':'DEAR','relative':'AIM','line':'LINEAIM',
    #         'med' : [{
    #             'medname':'para',
    #             'time':['08:00','12:00','20:30'],
    #             'quantity':'1',
    #                 'total':'10'},
    #                 {'medname':'coke',
    #                 'time':['12:00','17:00'],
    #                 'quantity':'1',
    #                 'total':'10'},
    #                 {'medname':'pepsi',
    #                 'time':['08:00','12:00'],
    #                 'quantity':'1',
    #                 'total':'10'}
    #                 ]}
    
    # for i in range(len(a['med'])):
    #     for j in range(len(a['med'][i]['time'])):
    #         print(i,a['med'][i]['time'][j])

    alarm_time = ["breakfast","lunch","dinner","bed"]
    alarm_med = []
    breakfast = "08:00"
    lunch = "12:00"
    dinner = "17:00"
    bed = "20:30"
    now = "08:00"
    # for i in range(len(a['med'])):
    #     for j in range(len(a['med'][i]['time'])):
    #         if now in a['med'][i]['time'][j]:
    #             alarm_med.append(a['med'][i]['medname'])
    # print(alarm_med)
    while True :
        print(now)
        if "20:39" == datetime.now().strftime("%H:%M"):
            #cozmosay
            print("YES")
            robot.say_text("DEAR").wait_for_completed()
            robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
            face_to_follow = robot.world.wait_for_observed_face(timeout=30)

            if face_to_follow:
            # start turning towards the face
                robot.say_text("Hey! DEAR it's time to take medicine!").wait_for_completed()
                turn_action = robot.turn_towards_face(face_to_follow)
        else :
            #line notify
            print("NO")
        time.sleep(10)