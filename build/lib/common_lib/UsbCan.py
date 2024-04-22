import os
import can

class UsbCan:
    """
    This class provides an interface to a USB-to-CAN adapter.

    Args:
        use (bool): True if the CAN adapter should be used, False if it should be ignored.
        bus (str): The name of the bus to use, e.g. 'can0'.

    Attributes:
        __state (bool): True if the CAN adapter is open, False if it is closed.
        __usemode (bool): True if the CAN adapter should be used, False if it should be ignored.
        __bus (str): The name of the bus to use, e.g. 'can0'.
        slcan (can.interface.Bus): The CAN interface object.

    """

    def __init__(self, use: bool, bus: str):
        self.__state = False
        self.__usemode = use
        self.__bus = bus
        return

    def open(self):
        """
        Open the USB-to-CAN adapter.

        Raises:
            OSError: If the CAN adapter cannot be opened.

        """
        if self.__usemode == True:
            self.__state = True
            try:
                self.slcan = can.interface.Bus(self.__bus, bustype='slcan', bitrate=1000000)
            except:
                print('Error')
            return

    def send(self, message):
        """
        Send a CAN message on the bus.

        Args:
            message (can.Message): The CAN message to send.

        Raises:
            OSError: If the CAN adapter is not open.

        """

        if self.__usemode == True:
            print("send")
            if self.__state == True:
                self.slcan.send(msg=message)
        print(message)
        return

    def receive(self):
        """
        Receive a CAN message on the bus.

        Returns:
            can.Message: The received CAN message, or None if no message is available.

        Raises:
            OSError: If the CAN adapter is not open.

        """
        if self.__state == True:
            msg = self.slcan.recv(0.001)
        else:
            msg = None
        return msg

# class CanMessage:
#     def __init__(self, arbitration_id: int, is_extended_id: bool, data):
#         msg = can.Message(
#             arbitration_id= arbitration_id,
#             is_extended_id= is_extended_id,
#             data= data
#         )
#         self.return_msg(msg)

#     def return_msg(self, message):
#         return message

