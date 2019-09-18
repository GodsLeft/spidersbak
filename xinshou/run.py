# coding:utf-8
from util.trainD2P import trainD2P
from util.extglobalfea import extglobalfea
from util.extlocalfea import extlocalfea
from util.extItmlclfea import extitemlclfea
from util.combinefea import combinefea
from util.labelfea import tolabelfea
import os

# 生成全局的商品子集的数据
if not os.path.exists('./data/gendata/data.csv'):
    trainD2P('data/item.csv', 'data/user.csv', 'data/gendata/data.csv')
else:
    print("data.csv already exist")

# 生成用户全局的购买数据
if not os.path.exists('./data/gendata/userglbfea.csv'):
    extglobalfea('data/user.csv', 'data/gendata/userglbfea.csv')
else:
    print("userglbfea.csv already exist")

# 用户的局部购买数据
if not os.path.exists('./data/gendata/userlclfea.csv'):
    extlocalfea('data/gendata/data.csv',
                'data/gendata/userlclfea.csv',
                '2014-12-15', '2014-12-19')
else:
    print("userlclfea.csv already exist")

# 商品的局部特征
if not os.path.exists('./data/gendata/itemlclfea.csv'):
    extitemlclfea('data/gendata/data.csv',
                  'data/gendata/itemlclfea.csv',
                  '2014-12-15', '2014-12-19')
else:
    print("itemlclfea.csv is already exist")

# 将所有的特征结合在一起
if not os.path.exists('./data/gendata/allfea.csv'):
    combinefea('data/gendata/data.csv',
               'data/gendata/userlclfea.csv',
               'data/gendata/userglbfea.csv',
               'data/gendata/itemlclfea.csv',
               'data/gendata/allfea.csv',
               '2014-12-15', '2014-12-19')
else:
    print("allfea.csv is already exist")

print("all fea done")

# 将特征打上标签
if not os.path.exists('./data/gendata/traindata.csv'):
    tolabelfea('data/gendata/data.csv', 'data/gendata/allfea.csv', 'data/gendata/traindata.csv',
             '2014-12-18', '2014-12-19')

# =====================================================

print("Test data----------")
if not os.path.exists('./data/gendata/userlclfea0.csv'):
    extlocalfea('data/gendata/data.csv',
                'data/gendata/userlclfea0.csv',
                '2014-12-16', '2014-12-20')
else:
    print("userlclfea0.csv already exist")

# 商品的局部特征
if not os.path.exists('./data/gendata/itemlclfea0.csv'):
    extitemlclfea('data/gendata/data.csv',
                  'data/gendata/itemlclfea0.csv',
                  '2014-12-16', '2014-12-20')
else:
    print("itemlclfea0.csv is already exist")

# 将所有的特征结合在一起
if not os.path.exists('./data/gendata/testdata.csv'):
    combinefea('data/gendata/data.csv',
               'data/gendata/userlclfea0.csv',
               'data/gendata/userglbfea.csv',
               'data/gendata/itemlclfea0.csv',
               'data/gendata/testdata.csv',
               '2014-12-16', '2014-12-20')

    # 结合特征之后可以删除局部性的文件
else:
    print("testdata.csv is already exist")

