import struct

def float_to_int_list(float_value: float) -> list[int]:
    # float型の値をバイナリに変換
    binary_data = struct.pack('<f', float_value)
    # バイナリデータをint型に変換し、8ビットずつリストに格納
    int_list = [int(byte) for byte in binary_data]

    return int_list

def int_list_to_float(int_list: list[int]) -> float:
    # int型のリストをバイナリデータに変換
    binary_data = bytes(int_list)
    # バイナリデータをfloat型に変換
    float_value = struct.unpack('<f', binary_data)[0]
    return float_value

def int_to_int_list(int_value: int, dlc: int) -> list[int]:
    data = int.to_bytes(int_value, length=dlc, byteorder='little')
    return [int(byte) for byte in data]