from datetime import datetime
import time
from detectqr import *
import json

import cozmo
import http.client
import asyncio


def follow_faces(robot: cozmo.robot.Robot):
    '''The core of the follow_faces program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    face_to_follow = None

    print("Press CTRL-C to quit")
    while True:
        turn_action = None
        if face_to_follow:
            # start turning towards the face
            turn_action = robot.turn_towards_face(face_to_follow)

        if not (face_to_follow and face_to_follow.is_visible):
            # find a visible face, timeout if nothing found after a short while
            try:
                face_to_follow = robot.world.wait_for_observed_face(timeout=30)
            except asyncio.TimeoutError:
                print("Didn't find a face - exiting!")
                return

        if turn_action:
            # Complete the turn action if one was in progress
            turn_action.wait_for_completed()

        time.sleep(.1)


def after_alarm(robot: cozmo.robot.Robot):
    # a = decodeQR()
    # a = json.loads(a.decode("utf-8").replace("'",'"'))
    # print(a)
    a = {
        'owner':'DEAR',
        'relative':'AIM',
        'line':'LINEAIM',
            'med' : [
                {
                    'medname': 'para',
                    'time': ['08:00','12:00','20:30'],
                    'quantity': '1',
                    'total': '10'
                },
                {
                    'medname': 'coke',
                    'time': ['12:00','17:00'],
                    'quantity': '1',
                    'total': '10'},
                {
                    'medname': 'pepsi',
                    'time': ['08:00','12:00'],
                    'quantity': '2',
                    'total': '10'
                }
                ]
            }

    # for i in range(len(a['med'])):
    #     for j in range(len(a['med'][i]['time'])):
    #         print(i,a['med'][i]['time'][j])

    # alarm_time = ["breakfast","lunch","dinner","bed"]
    # breakfast = "08:00"
    # lunch = "12:00"
    # dinner = "17:00"
    # bed = "20:30"
    now = datetime.now().strftime("%H:%M")
    

    # for i in range(len(a['med'])):
    #     for j in range(len(a['med'][i]['time'])):
    #         if now in a['med'][i]['time'][j]:
    #             alarm_med.append(a['med'][i]['medname'])
    # print(alarm_med)
    while True :
        alarm_med = []
        for i in range(len(a['med'])):
            for j in range(len(a['med'][i]['time'])):
                if "08:00" in a['med'][i]['time'][j]:
                    alarm_med.append({'name':a['med'][i]['medname'],'quantity':a['med'][i]['quantity']})
        # if "17:52" == datetime.now().strftime("%H:%M"):
            #cozmosay
        print("YES")
        robot.say_text("HEY! DEAR").wait_for_completed()
        robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
        face_to_follow = robot.world.wait_for_observed_face(timeout=30)

        if face_to_follow:
        # start turning towards the face
            robot.say_text("Hey! DEAR it's time to take medicine!, You have"+str(len(alarm_med))+"pills that you have to take").wait_for_completed()
            # turn_action = robot.turn_towards_face(face_to_follow)
            for k in alarm_med :
                robot.say_text("You have to take" + ' ' + k['name']  + ' ' + "only" + k['quantity']+ "tablet that you have to take").wait_for_completed()
        else :
            #line notify
            print("NO")
        time.sleep(10)
    
