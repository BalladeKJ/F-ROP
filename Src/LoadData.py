# 加载数据，获得数据集
# 输入：全路径列表
# 输出：数据集 -> list
from FileProcess import *
import Constants as C
from tqdm import tqdm


def load_data(rop_full_path: list, nonrop_full_path: list,
              windows_size=None, byte_cut=C.CUT_BYTE):
    """加载方差数据集
    Args:
        rop_full_path: rop文件全路径
        nonrop_full_path: 非rop文件全路径
        windows_size: 窗口大小
        byte_cut: 截断字节长度
        save_var_dataset: 是否保存方差数据集
    Return:
        dataset_x: 数据集x
        dataset_y: 标签数据集
        length: 输出维数大小 -> int
    """
    dataset_x = []; dataset_y = []
    print("Load ROP file...")
    for file in tqdm(rop_full_path):
        Bin = ExpMethod(file, windows_size=windows_size, byte_cut=byte_cut)
        dataset_x.append(Bin.var_list)
        dataset_y.append(1)
    print("Load NonROP file...")
    for file in tqdm(nonrop_full_path):
        Bin = ExpMethod(file, windows_size=windows_size, byte_cut=byte_cut)
        dataset_x.append(Bin.var_list)
        dataset_y.append(0)
    length = len(dataset_x[0])
    return dataset_x, dataset_y, length


def load_ori_data(rop_full_path, nonrop_full_path):
    """加载原始数据集
    Args:
        rop_full_path: rop文件全路径
        nonrop_full_path: 非rop文件全路径
    Return:
        dataset_x: 数据集x
        dataset_y: 标签数据集
    """
    dataset_x = []; dataset_y = []
    for file in tqdm(rop_full_path):
        Bin = ExpMethod(file)
        dataset_x.append(Bin.fix_int)
        dataset_y.append(1)
    for file in tqdm(nonrop_full_path):
        Bin = ExpMethod(file)
        dataset_x.append(Bin.fix_int)
        dataset_y.append(0)
    return dataset_x, dataset_y


def load_test_dataset(full_path, windows_size, byte_cut=C.CUT_BYTE):
    """加载测试用数据集，无标签
    Args:
        full_path: 文件全路径
    Return:
        dataset: 无标签数据集
    """
    dataset = []
    for file in full_path:
        Bin = ExpMethod(file, windows_size=windows_size, byte_cut=byte_cut)
        dataset.append(Bin.var_list)
    return dataset