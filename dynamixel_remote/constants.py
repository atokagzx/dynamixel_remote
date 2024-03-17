from enum import Enum


class Instruction(Enum):
    PING = 0x01
    READ_DATA = 0x02
    WRITE_DATA = 0x03
    REG_WRITE = 0x04
    ACTION = 0x05
    RESET = 0x06
    REBOOT = 0x08
    CLEAR = 0x10
    STATUS = 0x55
    SYNC_READ = 0x82
    SYNC_WRITE = 0x83
    FAST_SYNC_READ = 0x8A
    BULK_READ = 0x92
    BULK_WRITE = 0x93
    FAST_BULK_READ = 0x9A


class ControlTable:
    '''
    Control table addresses for the Dynamixel MX series
    Each entry is a tuple of the form (address_start, address_end(+1))
    '''
    ModelNumber = (0, 2)
    ModelInformation = (2, 6)
    FirmwareVersion = (6, 7)
    ID = (7, 8)
    BaudRate = (8, 9)
    ReturnDelayTime = (9, 10)
    DriveMode = (10, 11)
    OperatingMode = (11, 12)
    SecondaryID = (12, 13)
    ProtocolType = (13, 14)
    HomingOffset = (20, 24)
    MovingThreshold = (24, 28)
    TemperatureLimit = (31, 32)
    MaxVoltageLimit = (32, 34)
    MinVoltageLimit = (34, 36)
    PWMLimit = (36, 38)
    AccelerationLimit = (40, 44)
    VelocityLimit = (44, 48)
    MaxPositionLimit = (48, 52)
    MinPositionLimit = (52, 56)
    Shutdown = (63, 64)

    TorqueEnable = (64, 65)
    LED = (65, 66)
    StatusReturnLevel = (68, 69)
    RegisteredInstruction = (69, 70)
    HardwareErrorStatus = (70, 71)
    VelocityIGain = (76, 78)
    VelocityPGain = (78, 80)
    PositionDGain = (80, 82)
    PositionIGain = (82, 84)
    PositionPGain = (84, 86)
    Feedforward2ndGain = (88, 90)
    Feedforward1stGain = (90, 92)
    BUSWatchdog = (98, 99)
    GoalPWM = (100, 102)
    GoalVelocity = (104, 108)
    ProfileAcceleration = (108, 112)
    ProfileVelocity = (112, 116)
    GoalPosition = (116, 120)
    RealtimeTick = (120, 122)
    Moving = (122, 123)
    MovingStatus = (123, 124)
    PresentPWM = (124, 126)
    PresentLoad = (126, 128)
    PresentVelocity = (128, 132)
    PresentPosition = (132, 136)
    VelocityTrajectory = (136, 140)
    PositionTrajectory = (140, 144)
    PresentInputVoltage = (144, 146)
    PresentTemperature = (146, 147)


class OperatingMode(Enum):
    VELOCITY = 1
    POSITION = 3
    EXTENDED_POSITION = 4
    PWM_CONTROL = 16
    