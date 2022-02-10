# 测试原始流量效果
# 结果会在Result\\report.txt中
import Constants as C
from LoadData import load_ori_data
from FileProcess import get_full_path
import DeepLearningModel
from TrainModel import DeepLearningTrain
import os

model_name = "CNN_1D"
model_args = 1554
rop_full_path = get_full_path(C.ROP_TRAFFIC_PATH)
nonrop_full_path = get_full_path(C.NON_TRAIN_FILE)
accurary = []
dataset_x, dataset_y = load_ori_data(rop_full_path, nonrop_full_path)
DeepLearningTrain(model_name, model_args, dataset_x, dataset_y, batch=16, epochs=20)
