# 获得方差数据
from LoadData import load_data
from FileProcess import get_full_path
import os
import Constants as C
import multiprocessing
def chunker(data, chunk_num):
    length = len(data)
    chunk_vol = int(length / chunk_num)
    chunks = []
    for i in range(chunk_num):
        chunks.append(data[i*chunk_vol: (i+1) * chunk_vol])
    return chunks
nonrop_full_path = get_full_path(C.NON_TRAIN_FILE)
rop_full_path = get_full_path(C.ROP_TRAFFIC_PATH)
non_chunks = chunker(nonrop_full_path, 100)
rop_chunks = chunker(rop_full_path, 100)
    
if __name__ == '__main__':
    start = 5
    end = 8
    model_name = 'CNN_1D'
    for windows_size in range(start, end):
        dataset_x = []; dataset_y = []
        res = []
        p = multiprocessing.Pool(6)
        for i in range(len(non_chunks)):
            res.append(p.apply_async(load_data, (rop_chunks[i], non_chunks[i], windows_size)))
        for i in res:
            x, y, l = i.get()
            dataset_x.extend(x)
            dataset_y.extend(y)
        p.close()
        p.join()
        if(not os.path.exists(".\\Dataset\\Var_dataset\\" + str(windows_size))):
            os.mkdir(".\\Dataset\\Var_dataset\\" + str(windows_size))
        with open(".\\Dataset\\Var_dataset\\" + str(windows_size) + "\\dataset_x.txt", 'w') as f:
            f.write(str(dataset_x))
        with open(".\\Dataset\\Var_dataset\\" + str(windows_size) + "\\dataset_y.txt", 'w') as f:
            f.write(str(dataset_y))