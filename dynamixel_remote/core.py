import logging
import socket
import typing
import functools
from dynamixel_remote.constants import Instruction, ControlTable, OperatingMode
from dynamixel_remote.crc16 import compute_crc16
import struct


class DynamixelRemote:
    def __init__(self,
                 remote_host: str,
                 remote_port: int,
                 local_port: int):
        self._logger = logging.getLogger("dynamixel_remote")
        self._remote_host = remote_host
        self._remote_port = remote_port
        self._local_port = local_port
        self._bind_socket()
    

    def _bind_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(('', self._local_port))
        self._socket.settimeout(1)


    def _send_command(self, servo_id: bool, 
                      instruction: Instruction, 
                      params: bytes):
        self._validate_servo_id(servo_id)
        cmd = bytearray([0xFF, 0xFF, 0xFD, 0x00])
        cmd.append(servo_id)
        cmd.extend(struct.pack('<H', len(params) + 3))
        cmd.extend(struct.pack('B', instruction.value))
        cmd.extend(params)
        cmd.extend(compute_crc16(cmd))
        self._logger.debug("Sending command: %s", cmd)
        self._socket.sendto(cmd, (self._remote_host, self._remote_port))
        
    
    def turn_led(self, state: bool, 
                 servo_id: int,
                 wait_for_response: bool = False):
        instruction = Instruction.WRITE_DATA
        address = struct.pack('<H', ControlTable.LED[0])
        data = struct.pack('<H', int(state))
        params = address + data
        self._send_command(servo_id, instruction, params)
        if wait_for_response:
            response = self._socket.recv(1024)
            self._logger.debug("Received response: %s", response)
            return response


    def set_goal_position(self, position: int, 
                          servo_id: int):
        if position < 0 or position > 4095:
            raise ValueError("Position must be between 0 and 4095")
        instruction = Instruction.WRITE_DATA
        address = struct.pack('<H', ControlTable.GoalPosition[0])
        data = struct.pack('<l', position)
        params = address + data
        self._send_command(servo_id, instruction, params)

    
    def set_velocity(self, velocity: int,
                    servo_id: int):
        if velocity < -2047 or velocity > 2047:
            raise ValueError("Velocity must be between 0 and 2047")
        instruction = Instruction.WRITE_DATA
        address = struct.pack('<H', ControlTable.GoalVelocity[0])
        data = struct.pack('<l', velocity)
        params = address + data
        self._send_command(servo_id, instruction, params)


    def torque_enable(self, state: bool, 
                      servo_id: int):
        instruction = Instruction.WRITE_DATA
        address = struct.pack('<H', ControlTable.TorqueEnable[0])
        data = struct.pack('<H', int(state))
        params = address + data
        self._send_command(servo_id, instruction, params)


    def operating_mode(self, operating_mode: OperatingMode,
                       servo_id: int):
        assert isinstance(operating_mode, OperatingMode), "Operating mode must be an instance of OperatingMode enum"
        instruction = Instruction.WRITE_DATA
        address = struct.pack('<H', ControlTable.OperatingMode[0])
        data = struct.pack('<H', operating_mode.value)
        params = address + data
        self._send_command(servo_id, instruction, params)


    @staticmethod
    def _validate_servo_id(servo_id: int):
        if not (0 <= servo_id <= 0xFE):
            raise ValueError("Servo ID must be between 0 and 254")
    