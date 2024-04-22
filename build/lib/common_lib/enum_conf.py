from enum import IntEnum

class WheelType(IntEnum):
    OMNI_3 = 0
    OMNI_4 = 1
    MECHANUM = 2

class ControllerType(IntEnum):
    F310 = 1
    POTABLE = 0

class Reg(IntEnum):
    NOP = 0x0
    MOTOR_TYPE = 0x1
    CONTROL_TYPE = 0x2
    GEAR_RATIO = 0x3
    MOTOR_STATE = 0x4
    PWM = 0x10
    PWM_TARGET = 0x11
    SPD = 0x20
    SPD_TARGET = 0x21
    PWM_LIM = 0x22
    SPD_GAIN_P = 0x23
    SPD_GAIN_I = 0x24
    SPD_GAIN_D = 0x25
    POS = 0x30
    POS_TARGET = 0x31
    SPD_LIM = 0x32
    POS_GAIN_P = 0x33
    POS_GAIN_I = 0x34
    POS_GAIN_D = 0x35
    MONITOR_PERIOD = 0xF0
    MONITOR_REG = 0xF1

class GPIOReg(IntEnum):
    NOP = 0x0
    PORT_MODE = 0x1
    PORT_READ = 0x2
    PORT_WRITE = 0x3
    PORT_INT_EN = 0x4
    ESC_MODE_EN = 0x5
    PWM_PERIOD = 0x10
    PWM_DUTY = 0x20
    MONITOR_PERIOD = 0xF0
    MONITOR_REG = 0xF1


class EventType(IntEnum):
    PUSHDOWN = 0x0
    PULLUP = 0x1
    PUSHING = 0x2

class SHOOTING_STATUS(IntEnum):
    WAIT = 0 #ダクテッドが下、ベロがしまってある、押し出しが初期位置
    WAIT_2 = 5
    SHOOT_SET_1 = 1 #ダクテッドが上、ベロがしまってある、押し出しが初期位置
    SHOOT_SET_2 = 2 #ダクテッドが上、ベロが出ている、押し出しが初期位置
    SHOOT_WAIT = 3 #ダクテッドが上、ベロが出ている、押し出しが待機位置
    SHOOT = 4 #ダクテッドが上、ベロが出ている、押し出しが発射位置