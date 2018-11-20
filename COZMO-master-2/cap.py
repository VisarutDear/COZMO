import asyncio, functools, math, sys, cozmo
from cozmo.util import degrees, distance_mm, radians, speed_mmps, Vector2
from cozmo.lights import Color, Light
from PIL import Image, ImageColor, ImageDraw, ImageStat
import time
import cozmo
import asyncio

def a(robot):
    robot.move_lift(-3)   
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    time.sleep(1)
    robot.say_text("take a picture in" + ' '+ "3" + ' ' + "2" +' '+ "1").wait_for_completed()
    time.sleep(2)
    robot.camera.color_image_enabled = True
    imageA = robot.world.latest_image.raw_image
    imageA.save(("outA.png"), quality=100)

cozmo.run_program(a, use_viewer=True, force_viewer_on_top=True)
