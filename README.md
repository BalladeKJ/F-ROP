这些代码用于实现ROP攻击流量的检测。
# 实验需求
- python 3.x
- tensorflow 2.x
# 1. 数据集构建
输入命令：
>python3 ./Src/1-replaceGadget.py

将会生成包含ROP攻击流量保存在目录`ROP_traffic`下。

不同长度的ROP攻击流量保存在目录`./Length_ROP_traffic`下。

# 2. 模型训练
## 2.1 模型训练最佳窗口选择
输入命令：
>python3 ./Src/2-bestWindowsSize.py

可以得到训练模型保存在目录`./Model`下。

训练结果可以在`./Result/WindowsSize.txt`中查看。

## 2.2 未处理流量训练
训练未处理的流量,与实验2对比。
输入命令：
>python3 ./Src/3-originTrafficTrain.py

结果可以在`./Result/report.txt`中查看

## 2.3 机器学习模型对比测试
修改`./Src/4-modelCompare.py`中的
>windows_size = 11  # 改变窗口大小

修改模型注释，如：
>model = svm.SVC(kernel='rbf', C=0.5)

调整模型种类和参数。

输入命令：
>python3 ./Src/4-modelCompare.py
# 3. 模型测试
修改`./Src/5-errorTest.py`中的
>windows_size = 11

>model = 'CNN_W11.h5'

注意，窗口大小应与模型保持一致

输入命令：
>python3 ./Src/5-errorTest.py

即可得到结果。