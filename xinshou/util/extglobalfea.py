# coding:utf-8
import csv

def extglobalfea(userfile, gfea):
    """ 提取全局特征，用户的四类行为个数，购买商品种类个数 """
    with open(userfile) as ufile,\
            open(gfea, 'w') as gfeafile:

        fieldnames = ['user_id',
                      'bhvr_1', 'bhvr_2', 'bhvr_3', 'bhvr_4',
                      'item_n']

        reader = csv.DictReader(ufile)
        writer = csv.DictWriter(gfeafile, fieldnames=fieldnames)
        writer.writeheader()
        user_dict = {'user_id': '', 'bhvr_1': 0, 'bhvr_2': 0, 'bhvr_3': 0, 'bhvr_4': 0, 'item_n': 0}

        itemSet = set()
        flag = 1
        for row in reader:
            if row['user_id'] == user_dict['user_id']:
                user_dict['bhvr_'+row['behavior_type']] += 1
                itemSet.add(row['item_id'])
            else:
                if flag == 1:
                    flag -= 1
                else:
                    user_dict['item_n'] = len(itemSet)
                    writer.writerow(user_dict)
                itemSet.clear()
                user_dict['user_id'] = row['user_id']
                user_dict['bhvr_1'] = 0
                user_dict['bhvr_2'] = 0
                user_dict['bhvr_3'] = 0
                user_dict['bhvr_4'] = 0
                user_dict['item_n'] = 0
                itemSet.add(row['item_id'])
                user_dict['bhvr_'+row['behavior_type']] += 1
        # 为了最后一位用户信息
        user_dict['item_n'] = len(itemSet)
        writer.writerow(user_dict)
