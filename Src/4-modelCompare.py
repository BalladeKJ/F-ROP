# 进行模型对比
from sklearn.model_selection import cross_val_score
import sklearn
from LoadData import load_data
from sklearn import svm
from FileProcess import get_full_path
import Constants as C
from sklearn.ensemble import RandomForestClassifier 
from sklearn import linear_model
from sklearn.ensemble import GradientBoostingClassifier

windows_size = 11
rop_full_path = get_full_path(C.ROP_TRAFFIC_PATH)
nonrop_full_path = get_full_path(C.NON_TRAIN_FILE)
dataset_x, dataset_y, length = load_data(rop_full_path, nonrop_full_path, windows_size)
#model = svm.SVC(kernel='rbf', C=0.5)
#model = RandomForestClassifier(oob_score=True)
#model = linear_model.LogisticRegression()
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
print(windows_size, cross_val_score(model, dataset_x, dataset_y, cv=5, scoring='accuracy').mean())