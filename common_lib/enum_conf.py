from enum import IntEnum, Enum, auto

class WheelType(IntEnum):
    OMNI_3 = 0
    OMNI_4 = 1
    MECHANUM = 2

class F310_BTN(Enum):
    A = (0, 1)
    B = (1, 2)
    X = (2, 0)
    Y = (3, 3)
    LB = (4, 4)
    RB = (5, 5)
    LSTICK = (6, 10)
    RSTICK = (7, 11)

    def __init__(self, arr_id, btn_assign):
        super().__init__()
        self.arr_id = arr_id
        self.btn_assign = btn_assign
        return

class POTABLE_BTN(Enum):
    A = (0, 0)
    B = (1, 1)
    X = (2, 2)
    Y = (3, 3)
    LB = (4, 4)
    RB = (5, 5)
    LSTICK = (6, 9)
    RSTICK = (7, 10)

    def __init__(self, arr_id, btn_assign) -> None:
        super().__init__()
        self.arr_id = arr_id
        self.btn_assign = btn_assign
        return

class ControllerType(Enum):
    POTABLE = (0, POTABLE_BTN)
    F310 = (1, F310_BTN)

    def __init__(self, controller_id, btn_config) -> None:
        super().__init__()
        self.controller_id = controller_id
        self.btn_config = btn_config
        return

class RoboMasReg(IntEnum):
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

# class SHOOTING_STATUS(IntEnum):
#     WAIT = 0 #ダクテッドが下、ベロがしまってある、押し出しが初期位置
#     WAIT_2 = 5
#     SHOOT_SET_1 = 1 #ダクテッドが上、ベロがしまってある、押し出しが初期位置
#     SHOOT_SET_2 = 2 #ダクテッドが上、ベロが出ている、押し出しが初期位置
#     SHOOT_WAIT = 3 #ダクテッドが上、ベロが出ている、押し出しが待機位置
#     SHOOT = 4 #ダクテッドが上、ベロが出ている、押し出しが発射位置


class SHOOTING_STATUS(IntEnum):
    WAIT = auto() # 初期(一応ある)
    DUCTED_UP = auto() # ダクテッドを上げる
    PUSH_WAIT = auto() # 押し出し待機位置
    BERO_OUT = auto() # ベロを出す
    DUCTED_OFF = auto() # ダクテッドを切る
    # ここまで1シーケンス
    PUSH = auto() # 押し出し
    BERO_ORIGIN = auto() # ベロをしまう
    PUSH_ORIGIN = auto() # 押し出しを初期位置
    DUCTED_DOWN = auto() # ダクテッドを下げる
    # 0に戻す
    # ここまで1シーケンス
    SHOOT_MOTOR_ON = auto() # シューティングモーターを回す(強力)
    SHOOT_MOTOR_OFF = auto() # シューティングモーターを止める


class SPEED(Enum):
    SLOW = 1
    FAST = 3

class R_SPEED(Enum):
    SLOW = 1
    FAST = 2