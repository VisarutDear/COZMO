import asyncio
import sys
import asyncio, functools, math, sys, cozmo
from cozmo.util import degrees, distance_mm, radians, speed_mmps, Vector2
from cozmo.lights import Color, Light
from PIL import Image, ImageColor, ImageDraw, ImageStat
import time
import cozmo
import detectqr
from pyzbar.pyzbar import decode
from PIL import Image
import afteralarm

class BlinkyCube(cozmo.objects.LightCube):
    '''Subclass LightCube and add a light-chaser effect.'''
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._chaser = None

    def start_light_chaser(self):
        '''Cycles the lights around the cube with 1 corner lit up green,
        changing to the next corner every 0.1 seconds.
        '''
        if self._chaser:
            raise ValueError("Light chaser already running")
        async def _chaser():
            while True:
                for i in range(4):
                    cols = [cozmo.lights.off_light] * 4
                    cols[i] = cozmo.lights.green_light
                    self.set_light_corners(*cols)
                    await asyncio.sleep(0.1, loop=self._loop)
        self._chaser = asyncio.ensure_future(_chaser(), loop=self._loop)

    def stop_light_chaser(self):
        if self._chaser:
            self._chaser.cancel()
            self._chaser = None



# Make sure World knows how to instantiate the subclass
cozmo.world.World.light_cube_factory = BlinkyCube
def a(robot):
    robot.move_lift(-3)   
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    time.sleep(5)
    robot.camera.color_image_enabled = True
    imageA = robot.world.latest_image.raw_image
    imageA.save(("outA.png"), quality=100)


def cozmo_program(robot: cozmo.robot.Robot):
    cube = None
    cube = robot.world.get_light_cube(1)
    cube.start_light_chaser()
    cube.wait_for_tap(timeout=10)
    cube.stop_light_chaser()
    cube.set_lights_off()

    try:
        look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = robot.world.wait_for_observed_light_cube(timeout=60)
    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")
        return
    finally:
        look_around.stop()

    cube.start_light_chaser()
    try:
        print("Waiting for cube to be tapped")
        cube.wait_for_tap(timeout=10)
        print("Cube tapped")
    except asyncio.TimeoutError:
        print("No-one tapped our cube :-(")
    finally:
        a(robot)
        cube.stop_light_chaser()
        cube.set_lights_off()
        # res = decode(Image.open('outA.png'))
        # result = detectqr.decodeQR(res)
        afteralarm.after_alarm(robot)
        #robot.say_text(result).wait_for_completed()
        


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)