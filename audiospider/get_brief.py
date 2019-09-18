#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import jc_util
import http_util
from bs4 import BeautifulSoup


table_items = ['stock_code']
table_items += jc_util.fields_brief


def crawl_brief_data(stock_flag):
    """"""
    sub_url = jc_util.brief_url.format(stock_flag)
    req1 = http_util.get_req(sub_url)
    soup1 = BeautifulSoup(req1.text, 'lxml')
    results = []
    clears = soup1.find_all('div', class_='clear')
    for i in range(1):
        trs = clears[i].find_all('tr')
        for j in range(len(trs)):
            tds = trs[j].find_all('td')
            results.append([tds[0].text.strip(), tds[1].text.strip()])
    return results


def preprocess(raw_data):
    new_data = []
    for stock_code in raw_data.keys():
        row = raw_data[stock_code]
        new_row = [stock_code]
        for j in range(len(row)):
            title = row[j][0]
            content = row[j][1]
            if j in [0, 3]:
                if jc_util.has_cn(content):
                    content = content.replace(' ', '')
            if j in [6, 14, 15, 16]:  # delete comma in number
                content = content.replace(',', '')
            content = jc_util.unit_convert(title, content)
            new_row.append(content)
        new_data.append(new_row)
    return new_data


def crawl_all_data(stock_infos):
    raw_data = {}
    for stock_info in stock_infos:
        stock_flag = stock_info[2] + stock_info[0]
        raw_data[stock_info[0]] = crawl_brief_data(stock_flag)
        print('get stock_code: {} data from cninfo ok'.format(stock_info[0]))
    return raw_data


if __name__ == '__main__':
    stock_codes = jc_util.get_stock_code()
    print('get stock codes ok!')

    raw_brief_data = crawl_all_data(stock_codes)
    print('crawl data from web page ok!')

    new_brief_data = preprocess(raw_brief_data)
    print('preprocess raw data ok!')

    jc_util.store_into_db(new_brief_data, table_items)
    print('store data into database ok!')

