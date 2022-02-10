# 模型训练模块
import tensorflow as tf
import numpy as np
from sklearn.model_selection import StratifiedKFold
import Constants as C
import os
import DeepLearningModel

def evaluate(score=None, metrics=None, mean=False) -> dict:
    """用于评估模型性能
    Args:
        score: 评分，结构为[loss, accuracy, TP, TN, FP, FN]
        metrics: 评估指标字典结构为{'accuracy': [], 'precision': [], 'recall': [], 'false': [], 'miss': []}
        mean: 求平均模式，返回的字典value为float，默认为追加模式，返回的字典value为list
    Return:
        返回评估字典
    """
    if(mean == False):
        TP = score[2]; TN = score[3]; FP = score[4]; FN = score[5]
        metrics['accuracy'].append(score[1])
        metrics['precision'].append(TP / (TP + FP))
        metrics['recall'].append(TP / (TP + FN))
        metrics['false'].append(FP / (TN + FP))
        metrics['miss'].append(FN / (TP + FN))
    else:
        for key in metrics:
            metrics[key] = np.mean(metrics[key])
    return metrics


def DeepLearningTrain(model_name, model_args, dataset_x, dataset_y, value_k=5, batch=16, epochs=20, save_model_name=None, report=False):
    """深度学习训练
    Args:
        model_name: 深度学习模型名称
        model_args: 深度学习模型参数
        dataset_x: 数据集x
        dataset_y: 数据集标签
        value_k: 交叉验证k值
        batch: 数据集分批
        epochs: 训练迭代轮数
        save_model_name: 保存模型的名字 - 默认值不保存模型
        report: 是否生成报告:输入生成报告名,默认为不生成报告
    Return:
        metrics: 评价指标
    """
    max_acc = 0
    Kfold = StratifiedKFold(n_splits=value_k, shuffle=True, random_state=0)
    dataset_x = np.array(dataset_x)
    dataset_y = np.array(dataset_y)
    metrics = {'accuracy': [], 'precision': [], 'recall': [], 'false': [], 'miss': []}  # 评价指标
    acc = []
    for train, test in Kfold.split(dataset_x, dataset_y):
        model = DeepLearningModel.use_model(model_name, model_args)
        train_x = dataset_x[train]
        train_y = dataset_y[train]
        test_x = dataset_x[test]
        test_y = dataset_y[test]
        train_x=tf.expand_dims(train_x,-1)
        test_x=tf.expand_dims(test_x,-1)
        train_dataset=tf.data.Dataset.from_tensor_slices((train_x,train_y)).batch(batch).shuffle(100*batch)
        test_dataset=tf.data.Dataset.from_tensor_slices((test_x,test_y)).batch(batch)
        model.fit(train_dataset, epochs=epochs)
        score = model.evaluate(test_dataset, verbose=0)
        metrics = evaluate(score, metrics)
        print("Test accurary: " + str(score[1]))
        acc.append(score[1])
        if(acc[-1] > max_acc):
            max_acc = acc[-1]
            if(save_model_name != None):
                model.save(os.path.join(C.MODEL_PATH, save_model_name))
                print("Save model success!")
    metrics = evaluate(metrics=metrics, mean=True)
    print("Test accurary in {} fold: {}".format(value_k, acc))
    print("Mean accurary: {} Mean False: {} Mean Miss: {}\nMean Precision: {} Mean Recall: {}"
          .format(metrics['accuracy'], metrics['false'], metrics['miss'], metrics['precision'], metrics['recall']))
    print("Max accurary: {}".format(max_acc))
    if(report != False):
        reporter = []
        for key in metrics:
            reporter.append("{} : {}".format(key, metrics[key]))
        with open(".\\Result\\" + report, 'w') as f:
            f.write('\n'.join(reporter))
    return metrics