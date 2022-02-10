# 在正常流量中随机将一段字节替换为ROP链
# 最终输出含有ROP链的流量
# 1、将所有gadget替换文件储存至ROP_TRAFFIC_PATH中
# 2、将不同长度的gadget替换文件储存至ROP_LENGTH_TRAFFIC_PATH中
from itertools import count
from FileProcess import *
import os
import random
import Constants as C
from FileProcess import get_full_path

def replace_gadget(src_path, obj_path, replace_path, name):
    """将源路径片段替换目标路径文件，成功返回True,失败返回False
    """
    SrcBin = BinFile(src_path)
    ObjMal = BinFile(obj_path)
    if(SrcBin.bin_length > ObjMal.bin_length + C.CUT_BYTE):
        return False
    try:
        ObjMal.replace(SrcBin.bin_byte, start_site=C.CUT_BYTE)
    except:
        return False
    ObjMal.bin_write(replace_path, name=name)
    return True

def main(gadget_path, obj_path, replace_path, generate_num=10):
    """将gadget片段加入正常流量中
    Args:
        gadget_path: gadget片段的路径
        obj_path: 被替换流量目录路径
        relpace_path: 替换流量保存目录路径
        generate_num: 1个gadget片段生成替换流量数量,默认为10.
    """
    gadget_files = get_full_path(gadget_path)
    obj_files = get_full_path(obj_path)
    for file in gadget_files:
        if(".bin" not in file):
            continue
        num = 0
        while(num < generate_num):
            obj_file = random.sample(obj_files, 1)[0]
            if(replace_gadget(file, obj_file, replace_path, str(num+1) + "-" + os.path.basename(file))):
                num += 1

if __name__ == '__main__':
    ## 将所有gadget片段替换至正常流量中
    main(C.GADGET_PATH, C.NONROP_TRAFFIC_PATH, C.ROP_TRAFFIC_PATH)

    ## 将不同长度gadget片段替换至正常流量中
    for length_str in os.listdir(C.GADGET_LENGTH_PATH):
        if(not os.path.exists(os.path.join(C.ROP_LENGTH_TRAFFIC_PATH, length_str))):
            os.mkdir(os.path.join(C.ROP_LENGTH_TRAFFIC_PATH, length_str))
        main(os.path.join(C.GADGET_LENGTH_PATH, length_str), C.NONROP_TRAFFIC_PATH, os.path.join(C.ROP_LENGTH_TRAFFIC_PATH, length_str), 100)