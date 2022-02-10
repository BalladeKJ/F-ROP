# 进行一个图的画
from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Times New Roman'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
mpl.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内

def rgb255to1(rgb):
    if(type(rgb[0]) is list):
        return [[i / 255 for i in j]for j in rgb]
    return [i / 255 for i in rgb]

BLUE = rgb255to1([79, 129, 188])
GREEN = rgb255to1([146, 208, 80])
YELLOW = rgb255to1([255, 192, 0])
FEIHONG = rgb255to1([217, 149, 147])

RED_SERIES = rgb255to1([[214, 213, 183], [209, 186, 116], [230, 206, 172], [236, 173, 158], [244, 96, 108]])
BLUE_SERIES = rgb255to1([[68, 87, 102], [82, 111, 132], [122, 150, 171], [166, 186, 204], [209, 255, 233]])
print(YELLOW, FEIHONG)
print(RED_SERIES)

def compare():
    modelCom_y = [0.9701754450798035, 0.968421052631579, 0.9394736842105263, 0.913157894736842, 0.9267543859649123,0.7127192974090576]
    modelCom_x = ['CNN', 'RF', 'SVM', 'LR', 'GBDT','Original Traffic']
    color_ = [YELLOW, FEIHONG, FEIHONG, FEIHONG, FEIHONG, GREEN]
    plt.ylabel('Accuracy', size=16)
    plt.xlabel('Model Type', size=16)
    plt.bar(modelCom_x, modelCom_y, color=color_, width=0.5)
    plt.ylim([0.7, 1])
    plt.show()
def gadget():
    y = [
    0.7573333333333333, 0.826, 0.8813333333333333, 0.91, 0.9146666666666666,
    0.9573333333333334, 0.9726666666666667, 0.982, 0.9873333333333333,
    0.99, 0.9906666666666667, 0.9913333333333333, 0.9893333333333333, 0.9893333333333333,
    0.988, 0.9906666666666667, 0.992, 0.9953333333333333]
    x = [str(i) for i in range(8, 26)]
    plt.plot(x, y, '.-', color=BLUE, linewidth=2)
    plt.ylabel('Accuracy', size=16)
    plt.xlabel('ROP Chains Length', size=16)
    plt.ylim([0.75, 1])
    plt.grid()
    plt.show()
    
def windows():
    y = [0.9464912176132202, 0.9552631616592407, 0.9614035010337829,  0.9684210419654846,
        0.965350866317749, 0.9701754331588746, 0.9666666746139526, 0.9701754450798035,
        0.9701754331588746,  0.969298243522644, 0.9679824471473694, 0.9640350818634034,
        0.9649122834205628, 0.9644736886024475, 0.9657894730567932, 0.9679824709892273,
        0.9609648942947387]
    x = [str(i) for i in range(4, 21)]
    plt.plot(x, y, '.-', color=BLUE, linewidth=2)
    plt.ylabel('Accuracy', size=16)
    plt.xlabel('Window Size', size=16)
    plt.ylim([0.94, 0.98])
    plt.grid()
    plt.show()
# compare()
# windows()
gadget()