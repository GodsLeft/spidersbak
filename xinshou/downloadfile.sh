#!/usr/bin/env bash

# 自动获得我的登陆ip地址
ip=$(w | grep 'left' | awk '{print $3}' | grep '\.')

expect -c """
spawn scp data/gendata/testdata.csv \
            data/gendata/traindata.csv \
            $ip:~/Desktop/xinshou/data/gendata/

expect \"*password:*\"
send \"zhu@hadoop\\n\"
interact
"""
