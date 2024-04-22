from __future__ import annotations

from typing import Dict, List, Callable, Union

from enum import Enum

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

from enum_conf import *

class Button:
    """
    This class is used to handle the joy stick buttons.

    Args:
        Btn_assign (Union[F310_BTN]): A list of F310_BTN enums that represent the joy stick buttons.

    Attributes:
        __pushdown_event (Callable): The function to call when the pushdown event occurs.
        __pullup_event (Callable): The function to call when the pullup event occurs.
        __pushing_event (Callable): The function to call when the pushing event occurs.

    """

    def __init__(self):
        self.__pushdown_event: Callable = None
        self.__pullup_event: Callable = None
        self.__pushing_event: Callable = None

    def add_pushdown_event(self, event: Callable) -> None:
        """
        Adds a function to be called when the pushdown event occurs.

        Args:
            event (Callable): The function to call when the pushdown event occurs.

        Returns:
            None

        """
        self.__pushdown_event = event
        return

    def add_pullup_event(self, event: Callable) -> None:
        """
        Adds a function to be called when the pullup event occurs.

        Args:
            event (Callable): The function to call when the pullup event occurs.

        Returns:
            None

        """
        self.__pullup_event = event
        return

    def add_pushing_event(self, event: Callable) -> None:
        """
        Adds a function to be called when the pushing event occurs.

        Args:
            event (Callable): The function to call when the pushing event occurs.

        Returns:
            None

        """
        self.__pushing_event = event
        return

    def remove_pushdown_event(self) -> None:
        """
        Removes the function called when the pushdown event occurs.

        Returns:
            None

        """
        self.__pushdown_event = None
        return

    def remove_pullup_event(self) -> None:
        """
        Removes the function called when the pullup event occurs.

        Returns:
            None

        """
        self.__pullup_event = None
        return

    def remove_pushing_event(self) -> None:
        """
        Removes the function called when the pushing event occurs.

        Returns:
            None

        """
        self.__pushing_event = None
        return

    def detaminate_event(self, new, old):
        """
        This function is used to detect the changes in the joy stick buttons and trigger the corresponding events.

        Args:
            new (int): The new state of the button.
            old (int): The old state of the button.

        Returns:
            None

        """
        if new == 1 and old == 0:
            if self.__pushdown_event is not None:
                self.__pushdown_event()
            else:
                print("pushdown event not registered")
        elif new == 0 and old == 1:
            if self.__pullup_event is not None:
                self.__pullup_event()
            else:
                print("pullup event not registered")
        elif new == 1 and old == 1:
            if self.__pushing_event is not None:
                self.__pushing_event()
            else:
                print("pushing event not registered")
        else:
            pass


class JoyStick:
    pass

class Hat:
    pass
class Buttons:

    """
    This class is used to handle the joy stick buttons.

    Args:
        Btn_assign (Union[F310_BTN]): A list of F310_BTN enums that represent the joy stick buttons.

    Attributes:
        __btn_assign (Union[F310_BTN, POTABLE_BTN]): A list of F310_BTN enums that represent the joy stick buttons.
        __btns (List[Button]): A list of Button objects that represent the joy stick buttons.
        __old_btns (List[int]): A list of integers that represent the previous state of the joy stick buttons.

    """

    def __init__(self, Btn_assign: Union[F310_BTN, POTABLE_BTN]):
        self.__btn_assign = Btn_assign
        self.__btns = [Button() for i in range(8)]
        self.__old_btns = [0] * 8

    def detaminate_button(self, data: List[int]):
        """
        This function is used to detect the changes in the joy stick buttons and trigger the corresponding events.

        Args:
            data (List[int]): A list of integers representing the state of the joy stick buttons.

        Returns:
            None

        """
        for btn in self.__btn_assign:
            self.__btns[btn.arr_id].detaminate_event(
                data[btn.btn_assign], self.__old_btns[btn.arr_id]
            )
            self.__old_btns[btn.arr_id] = data[btn.btn_assign]
        return

    def add_event(self, index: int, event_type: int, event: Callable):
        """
        Adds an event to a button.

        Args:
            index (int): The index of the button.
            event_type (int): The type of event to add. Can be one of the EventType
                constants.
            event (Callable): The function to call when the event occurs.

        Raises:
            ValueError: If the event type is not recognized.

        """
        if event_type == EventType.PUSHDOWN:
            self.__btns[index].add_pushdown_event(event)
        elif event_type == EventType.PULLUP:
            self.__btns[index].add_pullup_event(event)
        elif event_type == EventType.PUSHING:
            self.__btns[index].add_pushing_event(event)
        else:
            raise ValueError(f"Invalid event type: {event_type}")

        return

    def detaminate_button(self, data: List[int]):
        """
        This function is used to detect the changes in the joy stick buttons and trigger the corresponding events.

        Args:
            data (List[int]): A list of integers representing the state of the joy stick buttons.

        Returns:
            None

        """
        for btn in self.__btn_assign:
            self.__btns[btn.arr_id].detaminate_event(
                data[btn.btn_assign], self.__old_btns[btn.arr_id]
            )
            self.__old_btns[btn.arr_id] = data[btn.btn_assign]
        return

    def add_event(self, index: int, event_type: int, event: Callable):
        """
        Adds an event to a button.

        Args:
            index (int): The index of the button.
            event_type (int): The type of event to add. Can be one of the EventType
                constants.
            event (Callable): The function to call when the event occurs.

        Raises:
            ValueError: If the event type is not recognized.

        """
        if event_type == EventType.PUSHDOWN:
            self.__btns[index].add_pushdown_event(event)
        elif event_type == EventType.PULLUP:
            self.__btns[index].add_pullup_event(event)
        elif event_type == EventType.PUSHING:
            self.__btns[index].add_pushing_event(event)
        else:
            raise ValueError(f"Invalid event type: {event_type}")

        return


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

    def __init__(self, arr_id, btn_assign):
        super().__init__()
        self.arr_id = arr_id
        self.btn_assign = btn_assign
        return


# For Debug mode
class TestNode(Node):
    def __init__(self) -> None:
        super().__init__("test_node")
        self.sub = self.create_subscription(Joy, "joy", self.callback, 10)
        self.button = Buttons(POTABLE_BTN)
        return

    def callback(self,data):
        self.button.detaminate_button(data.buttons)
        return

def main():
    rclpy.init()
    test_node = TestNode()
    rclpy.spin(test_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

