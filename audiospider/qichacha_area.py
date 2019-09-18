#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
在企查查网站，爬取公司名称
"""
import random
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=ue9331q8kc9fghpn62nsfmge13; UM_distinctid=16305980d0b465-0d80d7d8cfd1f6-3c604504-1fa400-16305980d0c51d; zg_did=%7B%22did%22%3A%20%2216305980d3b145-0c5b3566f6f6eb-3c604504-1fa400-16305980d3c3aa%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1524807241; acw_tc=AQAAAMSU70hVfwIAPUMYdI8VQc54V5Ix; _uab_collina=152480724949058518775424; _umdata=486B7B12C6AA95F2EBC93E57CA4D3AF20FECFACCB99B38AC0A88C3D55D90B76DF682257A48FD615ACD43AD3E795C914CF1D6E130197408C12A7570C534D0102E; CNZZDATA1254842228=966519044-1524806564-https%253A%252F%252Fwww.baidu.com%252F%7C1525062320; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201525065821554%2C%22updated%22%3A%201525067505486%2C%22info%22%3A%201524807241027%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%221910059864d8fa39de4f12d798dbb1ae%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1525067506',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url = 'http://www.qichacha.com/g_{}_{}.html'
code_file = 'code_area.txt'
comp_file = 'data_by_area/{}_comp.txt'


def get_area_code():
    """获取所有的地区的url"""
    req = requests.get(url.format('AH', '1'), headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    dls = soup.find_all('dl', class_='filter-tag clearfix')
    menleis = dls[0].find_all('a')
    fw = open(code_file, 'w', encoding='utf-8')
    for a in menleis:
        text = a.text.strip()
        fw.write('\t'.join([a['href'].split('.')[0].split('_')[1], text.split(' ')[0], text.split(' ')[2]]) + '\n')
    fw.close()


def get_code_from_file():
    """从文件当中获取url数据"""
    code_list = []
    with open(code_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            splits = line.strip().split('\t')
            code_list.append(splits[0])
    return code_list


def get_comp_name():
    """获取公司的名称"""
    code_list = get_code_from_file()
    for pidx in range(len(code_list)):
        # if pidx < 0:
        #     continue
        pair = code_list[pidx]
        i = 1
        fw = open(comp_file.format(pair), 'w', encoding='utf-8')
        while i < 501:
            time.sleep(random.random())
            cur_url = url.format(pair, str(i))
            req = requests.get(cur_url, headers=headers)
            # print(req.text)
            soup = BeautifulSoup(req.text, 'lxml')
            divs = soup.find_all('div', class_='col-md-12')
            sections = divs[1].find_all('section')
            if len(sections) == 0:
                continue
            for section in sections:
                name = section.find_all('span', class_='name')[0].text.strip()
                fw.write('\t'.join([pair, str(i), name]) + '\n')
            i += 1
        fw.close()


# get_area_code()
get_comp_name()
