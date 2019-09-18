#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import json
import datetime
import db_util


# table name
table_name = 'stock_info'

# URL
main_url = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
latest_url = 'http://www.cninfo.com.cn/information/lastest/{}.html'
brief_url = 'http://www.cninfo.com.cn/information/brief/{}.html'
brief_hk_url = 'http://www.cninfo.com.cn/information/hk/{}/brief{}.html'
issue_url = 'http://www.cninfo.com.cn/information/issue/{}.html'


# table fields in mysql
# 上市公司列表
# 股票代号，股票简称，所属板块，公司简称
fields_companylist = ['stock_code', 'stock_name', 'exchange', 'board']
fields_companylist_hk = ['stock_code', 'stock_name', 'exchange', 'board', 'comp_short_name']

# 最新资料
# 总股本，流通股，国家股，法人股，发起人股，转配股，B股，H股（单位：股）
# 每股收益(元)，每股资本公积金(元)，每股未分配利润(元)，净资产收益率(%)，每股净资产(元)
fields_latest = [
    'total_share', 'circulating_share', 'national_share', 'corporate_share', 'founder_share',
    'transferred_allotted_share', 'b_share', 'h_share',
    'earning_per_share', 'capital_reserve_per_share', 'undistributed_profits_per_share',
    'return_on_equity', 'net_assets_per_share'
]

# 公司概况
# 公司全称，英文名称，注册地址，公司简称，法定代表人，公司董秘，注册资本（元），行业种类，
# 邮政编码，公司电话，公司传真，公司网址，上市时间，招股时间，发行数量（股），发行价格（元）、
# 发行市盈率（倍），发行方式，主承销商，上市推荐人，保荐机构
fields_brief = [
    'comp_name', 'comp_name_en', 'registered_address', 'comp_short_name', 'legal_representative',
    'board_secretary', 'registered_capital', 'industry', 'post_code', 'comp_tel', 'comp_fax',
    'comp_url', 'listing_date', 'ipo_date', 'issue_share', 'issue_price', 'issue_pe_init',
    'issue_way_init', 'lead_underwriter', 'listing_recommender', 'sponsor_institution'
]

# 港股公司概况
# 公司全称，注册地址
fields_brief_hk = ['comp_name', 'registered_address']

# 发行筹资
# 发行类型，发行起始日，发行性质，发行股票种类，发行方式，发行公众股数量（股），
# 人民币发行价格（元），外币发行价格（元），实际募集资金（元），实际发行费用（元），
# 发行市盈率（倍），上网定价中签率（%），二级配售中签率（%）
fields_issue = [
    'issue_type', 'issue_start_date', 'issue_property', 'issue_stock_type', 'issue_way',
    'issue_public_share', 'issue_price_rmb', 'issue_price_foreign', 'actual_raise_capital',
    'actual_issue_cost', 'issue_pe', 'online_price_lottery_rate', '2nd_ration_lottery_rate'
]


def has_cn(input_str):
    flag = False
    for ch in input_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            flag = True
            break
    return flag


def unit_convert(title, content):
    if '万' in title and content != '':
        content = str(int(float(content) * 1e4))
    if '亿' in title and content != '':
        content = str(int(float(content) * 1e8))
    return content


def get_stock_code(exchange=None):
    conn, cur = db_util.get_cur()
    sql = "SELECT `stock_code`, `stock_name`, `board` FROM {} WHERE length(stock_code) = {}".\
        format(table_name, 6 if exchange is None else 5)
    results = db_util.execute_query(conn, cur, sql)
    cur.close()
    conn.close()
    return results


def update_item(conn, cur, stock_code, field, old_value, new_value, cur_time):
    # update item
    sql = "UPDATE {} SET `{}` = %s, update_time = %s WHERE `stock_code` = %s" .format(table_name, field)
    db_util.execute_query(conn, cur, sql, [new_value, cur_time, stock_code])
    # get update_log
    sql = "SELECT `update_log` FROM {} WHERE `stock_code` = %s".format(table_name)
    temp = db_util.execute_query(conn, cur, sql, [stock_code])
    json_log = [] if temp[0][0] is None or temp[0][0] == '' else json.loads(temp[0][0])
    json_log.insert(0, {'old_value': old_value, 'new_value': new_value,
                        'field': field, 'update_time': cur_time})
    # add record into update_log
    sql = "UPDATE {} SET `update_log` = %s WHERE `stock_code` = %s" .format(table_name)
    db_util.execute_query(conn, cur, sql, [json.dumps(json_log, ensure_ascii=False), stock_code])
    print('stock_code: {}, field: {}, old_value: {}, new_value: {}'.format(
        stock_code, field, old_value, new_value))


def store_into_db(results, table_items):
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('cur_time: {}'.format(cur_time))
    conn, cur = db_util.get_cur()
    update_cnt = 0
    insert_cnt = 0
    for result in results:
        new_result = [ele if ele != '' else None for ele in result]
        result = new_result
        stock_code = result[0]
        sql = "SELECT `{}` FROM {} WHERE `stock_code` = %s".format('`, `'.join(table_items), table_name)
        db_data = db_util.execute_query(conn, cur, sql, [stock_code])
        if len(db_data) == 0:  # if not found in db, insert
            sql = "INSERT INTO {}(`{}`, `insert_time`, `update_time`) VALUES(".format(
                table_name, '`, `'.join(table_items)) + "%s, " * (len(table_items) + 1) + "%s)"
            db_util.execute_query(conn, cur, sql, result + [cur_time, cur_time])
            insert_cnt += 1
        else:   # check which item need to update
            for item_idx in range(len(result)):
                field = table_items[item_idx]
                old_value = db_data[0][item_idx]
                new_value = result[item_idx]
                if str(new_value) == str(old_value):  # no change
                    continue
                if type(old_value) is float and new_value is not None and float(new_value) == old_value:
                    continue
                update_item(conn, cur, stock_code, field, old_value, new_value, cur_time)
                update_cnt += 1
    print('insert row num: {}\t update item num: {}'.format(insert_cnt, update_cnt))

