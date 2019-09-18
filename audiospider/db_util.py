#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""数据库操作类"""

import os
import configparser
import pymysql
import traceback
from pymongo import MongoClient


def load_config():
    """从admin.conf当中获取配置"""
    main_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    conf_path = os.path.join(os.path.join(main_dir, 'conf'), 'admin.conf')
    config = {}
    cf = configparser.ConfigParser()
    cf.read(conf_path)
    for section in cf.sections():
        for option in cf.options(section):
            config[option.upper()] = cf.get(section, option)
    return config


def get_cur():
    """获取数据库连接的游标"""
    config = load_config()
    conn = pymysql.connect(
        host=config['MYSQL_HOST'],
        port=int(config['MYSQL_PORT']),
        user=config['MYSQL_USER'],
        passwd=config['MYSQL_PASSWD'],
        db=config['MYSQL_DB'],
        charset='utf8'
    )
    cur = conn.cursor()
    return conn, cur


def execute_query(conn, cur, sql, data=None):
    results = []
    try:
        if data is None:
            cur.execute(sql)
        else:
            cur.execute(sql, data)
        if sql.startswith('SELECT'):
            results = cur.fetchall()
        else:
            conn.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(Exception, ':', e, '; Rollback')
        traceback.print_exc()
        conn.rollback()
    return results


def batch_execute_query(conn, cur, sql, data_list, batch_size=1000):
    n_samples = len(data_list)
    try:
        n_batch = n_samples // batch_size
        minibatch_start = 0
        for i in range(n_batch):
            minibatch = data_list[minibatch_start: minibatch_start + batch_size]
            cur.executemany(sql, minibatch)
            conn.commit()
            minibatch_start += batch_size
        if minibatch_start != n_samples:
            minibatch = data_list[minibatch_start:]
            cur.executemany(sql, minibatch)
            conn.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(Exception, ':', e, '; Rollback')
        traceback.print_exc()
        conn.rollback()


def get_mongo_conn():
    config = load_config()
    client = MongoClient(
        host=config['MONGO_HOST'],
        port=int(config['MONGO_PORT'])
    )
    db = client.knowledge_graph
    db.authenticate(config['MONGO_USER'], config['MONGO_PASSWD'])
    return db

