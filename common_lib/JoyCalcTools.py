# from enum_conf import *
from common_lib.enum_conf import ControllerType

class JoyCalcTools:
    def __init__(self, MODE):
        self.__MODE = MODE
        return

    def recalculate_joy(self, data):
        recalc_joy = [0] * 8
        if self.__MODE == ControllerType.POTABLE.controller_id:
            recalc_joy[0] = data.axes[0] * 1  #left-horizontal
            recalc_joy[1] = data.axes[1] * -1  #left-vertical
            recalc_joy[2] = data.axes[3] * -1  #right-horizontal
            recalc_joy[3] = data.axes[4] * -1  #right-vertical
            recalc_joy[4] = data.axes[2] * 1 + 1 #left-trigger
            recalc_joy[5] = data.axes[5] * 1 + 1 #right-trigger
            recalc_joy[6] = 0 #none
            recalc_joy[7] = 0 #none
        elif self.__MODE == ControllerType.F310.controller_id:
            recalc_joy[0] = data.axes[0] * 1  #left-horizontal
            recalc_joy[1] = data.axes[1] * -1  #left-vertical
            recalc_joy[2] = data.axes[2] * -1  #right-horizontal
            recalc_joy[3] = data.axes[3] * 1  #right-vertical
            recalc_joy[4] = 0 #none
            recalc_joy[5] = 0 #none
            recalc_joy[6] = 0 #none
            recalc_joy[7] = 0 #none

        recalc_joy = list(map(float, recalc_joy))
        print("recalc:", recalc_joy)

        return recalc_joy