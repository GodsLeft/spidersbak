#coding:utf-8

def getrealname(infile, outfile):
    with open(infile, 'r') as IN:
        with open(outfile, 'w') as OUT:
            for line in IN.readlines():
                #print line
                tokens = line.strip().split(",")
                if len(tokens) != 2:
                    continue
                name = tokens[1]
                OUT.write(name + "\n")

                if name.find("(") != -1:
                    realname = name[0:name.index("(")]
                    OUT.write(realname + "\n")

# 去除店名的重复
def rmrepeat(infile, outfile):
    Names = set()
    notin = 0
    allcn = 0
    with open(infile, 'r') as IN:
        with open(outfile, 'w') as OUT:
            for line in IN.readlines():
                allcn += 1
                name = line.strip()
                if name not in Names:
                    notin += 1
                    Names.add(name)
                    OUT.write(name + "\n")

    print "allcn #### ", allcn
    print "notin #### ", notin

#getrealname("../data/food.csv", "../data/foodname.txt")
#getrealname("../data/hotel.csv", "../data/hotelname.txt")
#getrealname("../data/shop.csv", "../data/shopname.txt")

rmrepeat("../data/foodname.txt", "../data/foodname2.txt")
#rmrepeat("../data/hotelname.txt", "../data/hotelname2.txt")
#rmrepeat("../data/shopname.txt", "../data/shopname2.txt")
