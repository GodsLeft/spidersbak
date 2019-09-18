#coding:utf-8
from pandas import Series
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

from sklearn.linear_model import LogisticRegression
#from sklearn import preprocessing
#from sklearn.svm import SVC

def prtMsg(expected, predicted, model=None):
    if model:
        print model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print(metrics.precision_score(expected, predicted))
    print(metrics.recall_score(expected, predicted))
    print(metrics.f1_score(expected, predicted))


def trainModeltest(model, traindata, testdata):
    y = traindata['label']
    X = traindata.drop(['cat','label'], axis=1)
    model.fit(X,y)
    predicted = model.predict(X)
    prtMsg(y, predicted, model)

    y = testdata['label']
    X = testdata.drop(['cat','label'], axis=1)
    predicted = model.predict(X)

    pred = Series(predicted, index=X.index)
    pred[pred==1].to_csv('./vs.csv')

model = DecisionTreeClassifier(max_depth=7)
lrModel = LogisticRegression(C=1.0,penalty='l2')

# 这条命令只能在命令行中运行了
#trainModeltest(model, traindata, testdata)







#X = data[['bhvrT1','bhvrT2','bhvrT3','bhvrT4','time',\
#          'ibh1','ibh2','ibh3','ibh4',\
#          'gbh1','gbh2','gbh3','gbh4']]


#data['dtpred'] = predicted
#DTVS = data[['label','dtpred']]
#DTVS[DTVS['dtpred']==1].to_csv('./vs.csv')

#yes.to_csv('./vs.csv')
#y_pred_index = Series(y_pred, index=X.index)
#np.concatenate([y, y_pred.ravel()])
#pd.concat([y, y_pred_index], axis=1)
"""
X_1 = preprocessing.normalize(X)
X_2 = preprocessing.scale(X)

C = 1.0
lrModel = LogisticRegression(C=C,penalty='l2')
lrModel.fit(X_2, y)
pred = lrModel.predict(X_2)
# data['pred'] = pred
# vs = data[['label','pred']]
# print pred.sum()
# print vs[vs['pred']==1]
"""

