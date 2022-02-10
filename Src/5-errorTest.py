# 误报、漏报测试
from ModelTest import model_test
from FileProcess import get_full_path
import Constants as C


windows_size = 11   # 在这里输入窗口大小
model = 'CNN_W11.h5'
full_path = get_full_path(C.CVE_TRAFFIC_PATH)
model_test(model, full_path, windows_size, symbol='<')
full_path = (C.NONROP_TRAFFIC_PATH)
model_test(model, full_path, windows_size, symbol='>')