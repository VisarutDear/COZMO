

import cozmo
import http.client
import asyncio

def a(robot):
    b1 = {  'med' : [
                {
                    'medname': 'para',
                    'time': ['08:00','12:00','20:30'],
                    'quantity': '1',
                    'total': '10'
            }]}
    robot.say_text("This medicine name" + '     ' + b1['med'][0]['medname']  + '    ' + "You have to take on" + \
   ' '+ " breakfast lunch and dinner "+ "for" + ' ' + b1['med'][0]['quantity'] + '' + "tablets").wait_for_completed()

cozmo.run_program(a, use_viewer=True, force_viewer_on_top=True)