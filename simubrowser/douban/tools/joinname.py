#!/usr/bin/env python
# -*- coding:utf8 -*-

def name2aname(namefile, outfile):
    with open(namefile, 'r') as IN, open(outfile, 'w') as OUT:
        ab = []
        for line in IN:
            if line.strip() == "####":
                OUT.write('\t'.join(ab) + "\n")
                ab = []
            else:
                ab.append(line.strip())

if __name__ == '__main__':
    name2aname("test01", "outfile")