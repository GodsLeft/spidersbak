# coding:utf-8

import pandas as pd

# 删除第一行和第一列
def tofeaturefile(input, output):
    df = pd.read_csv(input)
    df[1:].to_csv(output, header=False)