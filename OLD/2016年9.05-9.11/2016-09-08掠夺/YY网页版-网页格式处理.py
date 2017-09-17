from pyquery import PyQuery as PYQ
import re


def rp_fun(list_str):
    rp = re.sub("^.*梦◥", "", list_str)
    rp1 = re.sub("\s*【.*$", "", rp)
    return rp1

Doc = open('YY.txt', 'r', encoding='utf-8')
YY_List = PYQ(Doc.read())
Member_List = YY_List('.name-nick')

with open('YY_List.txt', 'w', encoding='utf-8') as f:
    for i in Member_List:
        new_list = rp_fun(PYQ(i).text())
        f.write(new_list+'\n')