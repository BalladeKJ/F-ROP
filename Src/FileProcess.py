from math import perm
import os
import re
import random
import ByteTools
import numpy as np
import matplotlib

class BinFile:
    """二进制文件类，储存二进制文件信息，处理二进制文件
    参数:
        - name_path 路径+文件名 如:./dataset/1234-1.bin
    """
    def __init__(self, name_path : str) -> None:
        self.name_path = name_path  # 字节流文件路径
        self.bin_length = 0    # 字节流文件长度
        self.bin_file_name = None # 文件名
        self.dir_path = None    # 目录路径
        self.bin_byte = None    # 文件字节流
        self.get_base_imformation()


    def get_base_imformation(self):
        """文件获得基本信息信息
        包括:
            self.dir_path
            self.bin_file_name
            self.bin_byte
            self.file_num
            self.bin_length
        """
        self.dir_path = '\\'.join(self.name_path.split('\\')[:-1])
        self.bin_file_name = self.name_path.split('\\')[-1]
        with open(self.name_path, 'rb') as file:
            self.bin_byte = file.read()
        self.bin_length = len(self.bin_byte)


    def bin_write(self, write_dir_path='./', name=None):
        """向文件中写入字节流bin_byte
        参数:
            - write_dir_path 写入目录路径，默认为当前路径
        """
        if(not os.path.exists(write_dir_path)):
            os.mkdir(write_dir_path)
        if(name == None):
            name = self.bin_file_name
        with open(os.path.join(write_dir_path, name), 'wb') as file:
            file.write(self.bin_byte)


    def replace(self, input_byte: bytes, site=None, start_site=0):
        """在字节流中以input字节替换
        参数:
            - input_byte 替换字节
            - site 替换位置，默认为随机
            - start_site 能开始替换的起始字节
        """
        bin_byte = self.bin_byte.decode("raw_unicode_escape")
        input_byte = input_byte.decode("raw_unicode_escape")
        input_length = len(input_byte)
        max_site = self.bin_length - input_length
        if(site == None):
            site = random.randint(start_site, max_site)
        bin_byte = bin_byte[0:site] + input_byte + bin_byte[site + input_length:]
        assert(len(bin_byte) == self.bin_length)
        self.bin_byte = bin_byte.encode("raw_unicode_escape")
        return self.bin_byte


class ExpMethod(BinFile):
    """我们的实验

    Args:
        BinFile (BinFile): 父类
    """
    def __init__(self, name_path: str, fix_length=1554, windows_size=None, byte_cut=0) -> None:
        super().__init__(name_path)
        self.CHANNAL = 4
        self.windows_size = windows_size    # 滑动窗口大小
        self.fix_length = fix_length    # 字节流固定长度
        self.byte4channal = None    # 4通道字节流
        self.var_list = None    # 4通道字节流滑动方差
        self.byte_cut = byte_cut   # 字节流截断值
        self.fix_int = None    # 定长字节流的int形式
        self.get4channal_flow()
        if(windows_size != None):
            self.get_var_list()


    def get4channal_flow(self):
        """从文件中获取四通道字节流
        获得:
            self.byte4channal
        """
        data_flow = [0 for i in range(self.fix_length - self.byte_cut)]
        byte =  self.bin_byte[self.byte_cut:]
        byte = ByteTools.byte2int(byte)
        for i in range(len(byte)):
            data_flow[i] = byte[i]
        self.fix_int = data_flow
        data_flow = ByteTools.cut(data_flow, self.CHANNAL)
        if(len(data_flow[-1]) != self.CHANNAL):
            del data_flow[-1]
        data_flow = np.array(data_flow).T
        data_flow = list(data_flow)
        self.byte4channal = data_flow
        return data_flow


    def get_var_list(self):
        """获得方差
        """
        data =  self.byte4channal
        length = len(data[0])
        result = []
        for i in range(length - self.windows_size + 1):
            single_result = []
            for j in range(self.CHANNAL):
                windows = data[j][i:i + self.windows_size]
                single_result.append(len(set(windows)))
            result.append(np.var(single_result))
        self.var_list = result
        return result
    
    
def get_full_path(directory, suffix='.bin'):
    """获得所有某后缀文件的全路径,有从文件中加载和从路径中加载两种方式
    参数:
        - directory 获得此目录下文件或文件名
    """
    all_path = []
    if(os.path.isdir(directory)):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if(suffix in file):
                    all_path.append(os.path.join(root, file))
                    
    elif(os.path.isfile(directory)):
        with open(directory, 'r') as f:
            all_path = f.read().splitlines()
    return all_path
