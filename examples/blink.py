#!/usr/bin/env python3

import time
from dynamixel_remote import DynamixelRemote as dxlr

remote_host = "10.0.10.16"
remote_port = 40004
local_port = 40000
servo_id = 1

if __name__ == "__main__":
    servo_hub = dxlr(remote_host, remote_port, local_port)
    while True:
        try:
            print(servo_hub.turn_led(True, servo_id, wait_for_response=True))
            time.sleep(1)
            servo_hub.turn_led(False, servo_id)
            time.sleep(1)
        except KeyboardInterrupt:
            break
