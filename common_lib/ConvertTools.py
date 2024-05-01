import struct
"""
This function converts a float value to a list of integers using the struct module.

:param float_value: The float value to convert
:type float_value: float
:return: A list of integers representing the binary representation of the float value
:rtype: list[int]
"""
def float_to_int_list(float_value: float) -> list[int]:
    # float型の値をバイナリに変換
    binary_data = struct.pack('<f', float_value)
    # バイナリデータをint型に変換し、8ビットずつリストに格納
    int_list = [int(byte) for byte in binary_data]

    return int_list

"""
This function converts a list of integers back to a float value using the struct module.

:param int_list: The list of integers representing the binary representation of the float value
:type int_list: list[int]
:return: The float value represented by the list of integers
:rtype: float
"""
def int_list_to_float(int_list: list[int]) -> float:
    # int型のリストをバイナリデータに変換
    binary_data = bytes(int_list)
    # バイナリデータをfloat型に変換
    float_value = struct.unpack('<f', binary_data)[0]
    return float_value

"""
This function converts an integer value to a list of integers using the int.to_bytes() method.

:param int_value: The integer value to convert
:type int_value: int
:param dlc: The desired length of the resulting list of integers
:type dlc: int
:return: A list of integers representing the binary representation of the integer value
:rtype: list[int]
"""
def int_to_int_list(int_value: int, dlc: int) -> list[int]:
    data = int.to_bytes(int_value, length=dlc, byteorder='little')
    return [int(byte) for byte in data]