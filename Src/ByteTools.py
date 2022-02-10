## 工具集，对比特流进行处理
import struct
def byte2int(byte_flow) -> list:
    """byte流转int列表
    """
    byte_flow = list(byte_flow)
    for i in range(len(byte_flow)):
        byte_flow[i] = int(byte_flow[i])
    return byte_flow


def int2byte(int_list):
    """int列表转byte流
    """
    byte_flow = b''
    for i in int_list:
        byte_flow += struct.pack('B', i)
    return byte_flow


def cut(obj, sec):
    """将byte流按sec字节切分
    """
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]
