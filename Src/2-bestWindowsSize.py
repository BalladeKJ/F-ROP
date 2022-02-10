# 训练模型以获得最好的窗口大小
# 模型参数保存在Model目录下
import Constants as C
from LoadData import load_data
from FileProcess import get_full_path
from TrainModel import DeepLearningTrain
import os
import random

nonrop_full_path = random.sample(get_full_path(C.NONROP_TRAFFIC_PATH), 1400)
with open(os.path.join(C.NON_TRAIN_FILE), 'w') as f:
    f.write('\n'.join(nonrop_full_path))
rop_full_path = get_full_path(C.ROP_TRAFFIC_PATH)
nonrop_full_path = get_full_path(C.NON_TRAIN_FILE)

accurary = [] 
start = 5
end = 21
model_name = 'CNN_1D'
with open(os.path.join(C.RESULT_PATH, "WindowsSize.txt"), 'w') as f:
    pass
for windows_size in range(start, end):
    dataset_x, dataset_y, length = load_data(rop_full_path, nonrop_full_path, windows_size)
    print(length)
    DeepLearningTrain(model_name, length, dataset_x, dataset_y, batch=16,
                    epochs=20,save_model_name='CNN_W{}.h5'.format(str(windows_size)), report='report.txt', value_k=5)
    with open(os.path.join(C.RESULT_PATH, "WindowsSize.txt"), 'a+') as f:
        with open(os.path.join(C.RESULT_PATH, "report.txt"), 'r') as f1:
            f.write(str(windows_size) + ':\n' + f1.read() + '\n')
