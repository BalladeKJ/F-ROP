# 用于模型性能测试
import tensorflow as tf
import os
import Constants as C
from LoadData import load_test_dataset

def model_test(model_name, full_path: list, windows_size, error_name="error.txt", symbol='<') -> list:
    """模型测试函数
    Args:
        model_name: 保存模型的名字
        full_path: 测试文件全路径
        windows_size: 窗口大小
        error_name: 存储错误信息的名字，默认为 error.txt
        symbol: 符号，可以决定输出误报还是漏报，>表示漏报率，<表示误报率
    Return:
        error: 错误的文件全路径列表
        error_rate: 错误率
    """
    model = tf.keras.models.load_model(os.path.join(C.MODEL_PATH, model_name))
    dataset = load_test_dataset(full_path, windows_size=windows_size)
    dataset=tf.expand_dims(dataset,-1)
    predict_classes = model.predict(dataset)
    error = []
    for i, result in enumerate(predict_classes):
        if(symbol == '<'):
            if(result[0] < 0.5):
                error.append(full_path[i])
        else:
            if(result[0] > 0.5):
                error.append(full_path[i])        
    with open(os.path.join(".\\Result", error_name), 'w') as file:
        file.write('\n'.join(error))
    error_rate = len(error) / len(predict_classes)
    print("错误率:{}".format(error_rate))
    return error, error_rate
