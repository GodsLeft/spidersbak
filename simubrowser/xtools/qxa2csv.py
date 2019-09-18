#coding:utf-8
import re

def qxa2csv01(qxafile, result):
    with open(qxafile, 'r') as QXA, open(result, 'w') as RES:
        mode = re.compile("华泰客服 \d+-\d+-\d+ \d:\d:\d")
        while True:
            line = QXA.readline()
            if line != '':
                if line.strip() == "####":
                    RES.write("\n")
                    RES.write(QXA.readline().strip() + "\t\t")
                    QXA.readline()    # 抛弃第二行
                else:
                    RES.write(line.strip() + " ")
            else:
                break

def tsv2all(tsv, out):
    with open(tsv, 'r') as TSV, open(out, 'a') as OUT:
        OUT.writelines(TSV.readlines())

if __name__ == '__main__':
    # 生成10个tsv文件
    # for i in range(10):
    #     input = "../data/qxa0" + str(i) + ".txt"
    #     output = "../data/tsvresult/qxa0" + str(i) + ".tsv"
    #     qxa2csv01(input, output)

    # for i in range(10):
        # tsv = "../data/tsvresult/qxa0" + str(i) + ".tsv"
        # out = "../data/tsvresult/allqxa.tsv"
        # tsv2all(tsv, out)

    #for i in range(1, 10):
    #    tsv = "../data/tsvresult/qxa0" + str(i) + ".tsv"
    #    out = "../data/tsvresult/allqxa_1_10.tsv"
    #    tsv2all(tsv, out)


    #生成10个tsv文件
    for i in range(11, 16):
        input = "../data/qxa" + str(i) + ".txt"
        output = "../data/tsvresult/qxa" + str(i) + ".tsv"
        qxa2csv01(input, output)

    for i in range(11, 16):
        tsv = "../data/tsvresult/qxa" + str(i) + ".tsv"
        out = "../data/tsvresult/allqxa_11_15.tsv"
        tsv2all(tsv, out)
