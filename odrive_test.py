import json
import math as math
import sys
import time

import numpy as np
import odrive
from odrive.enums import *

odrv0 = odrive

def start():
    global odrv0
    print("finding odrive")
    odrv0 = odrive.find_any()

def idle():
    global odrv0
    odrv0.axis0.requested_state = AXIS_STATE_IDLE
    odrv0.axis1.requested_state = AXIS_STATE_IDLE

def close():
    global odrv0
    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  

def move(x):
    global odrv0
    odrv0.axis0.controller.move_incremental(x,False)
    odrv0.axis1.controller.move_incremental(x,False) 

def odQuit():
    global odrv0
    odrive.quit()         

def main():
    start()
    close()
    for i in range(10):
        move(1000)
        time.sleep(3.0)
        move(-1000)
        time.sleep(3.0)
    idle()
    time.sleep(3.0)
    odQuit()
if __name__ == '__main__':
    main()            
