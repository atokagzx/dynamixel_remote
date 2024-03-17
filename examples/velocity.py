#!/usr/bin/env python3

import time
from dynamixel_remote import DynamixelRemote as dxlr
from dynamixel_remote import OperatingMode

remote_host = "10.0.10.16"
remote_port = 40004
local_port = 40000
servo_id = 1

if __name__ == "__main__":
    servo_hub = dxlr(remote_host, remote_port, local_port)
    servo_hub.operating_mode(OperatingMode.VELOCITY, servo_id)
    servo_hub.torque_enable(True, servo_id)
    while True:
        try:
            servo_hub.set_velocity(100, servo_id)
            time.sleep(0.3)
            servo_hub.set_velocity(-100, servo_id)
            time.sleep(0.3)
        except KeyboardInterrupt:
            servo_hub.torque_enable(False, servo_id)
            break
        