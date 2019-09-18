#coding:utf-8
import numpy as np
#from pandas import Series

from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import metrics
# from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def prtMsg(expected, predicted, model=None):
    if model:
        print model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print(metrics.precision_score(expected, predicted))
    print(metrics.recall_score(expected, predicted))
    print(metrics.f1_score(expected, predicted))

def lgRegModel(traindata, testdata):
    y = traindata['label']
    X = traindata.drop(['cat','label'],axis=1)

    #X_1 = preprocessing.normalize(X)
    X_2 = preprocessing.scale(X)

    C = 1.0
    lrModel = LogisticRegression(C=C,penalty='l2')
    lrModel.fit(X_2, y)
    pred = lrModel.predict(X_2)
    prtMsg(y, pred)

def DTModel(traindata, testdata):
    y = traindata['label']
    X = traindata.drop(['cat','label'], axis=1)
    model = DecisionTreeClassifier()
    model.fit(X,y)
    expected = y
    predicted = model.predict(X)
    prtMsg(expected, predicted, model)

    y = testdata['label']
    X = testdata.drop(['cat','label'],axis=1)
    expected = y
    predicted = model.predict(X)
    prtMsg(expected, predicted)

def balancedata(x):
    if x['label'] == 0 and np.random.rand() > 0.004*5:
        x['label'] = np.nan
    return x
def timefilter(x):
    if x['time'] > 36:
        x['time'] = np.nan
    return x


def trainModeltestT(model, traindata, testdata):
    y = traindata['label']
    X = traindata.drop(['cat','label'], axis=1)
    model.fit(X, y)
    predicted = model.predict(X)
    prtMsg(y, predicted, model)

    y = testdata['label']
    X = testdata.drop(['cat','label'], axis=1)
    predicted = model.predict(X)
    prtMsg(y, predicted, model)


def runT(traindataT, testdataT):
    print "="*20
    model = DecisionTreeClassifier(max_depth=7)
    trainModeltestT(model, traindataT, testdataT)

#lgRegModel(traindata, testdata)
#DTModel(traindata, testdata)





#======================================
#X = traindata[['gbh3','gbh4','gitm','lbh3','lbh4','litm','bhvrT4','ibh4']]
#yP = model.predict(X)
#yPs = Series(yP, index=X.index)
#yPs[yPs == 1].to_csv('./vs.csv')

#data['dtpred'] = predicted
#DTVS = data[['label','dtpred']]
#DTVS[DTVS['dtpred']==1].to_csv('./vs.csv')

#yes.to_csv('./vs.csv')
#y_pred_index = Series(y_pred, index=X.index)
#np.concatenate([y, y_pred.ravel()])
#pd.concat([y, y_pred_index], axis=1)
