# coding:utf-8

import csv
"""
@Author:left
@description: 根据商品子集，将用户数据分离一部分出来
"""

def trainD2P(condfile, itemDfile, itemPfile):
    '''
    @parameter1:商品子集
    @parameter2:用户的所有行为数据
    @parameter3:用户在这个子集上的行为
    @description:问题是这样割裂了商品之间的关联,比如商品聚类
    '''
    with open(condfile) as cfile,\
        open (itemDfile) as Dfile,\
        open(itemPfile,'w') as Pfile:

        fieldnames = ['user_id','item_id','behavior_type',\
                      'user_geohash','item_category','time']

        creader = csv.DictReader(cfile)
        Cset = set()
        for row in creader:
            Cset.add(row['item_id'])

        Dreader = csv.DictReader(Dfile)
        Pwriter = csv.DictWriter(Pfile, fieldnames=fieldnames)
        Pwriter.writeheader()
        for row in Dreader:
            if row['item_id'] in Cset:
                Pwriter.writerow(row)

# 将item中的数据作为条件，过滤用户行为数据
# trainD2P('data/item.csv','data/user.csv','./data/data.csv')
