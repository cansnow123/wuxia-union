from pyquery import PyQuery as PYQ
import re

def rpfun(list_str):
    rp_1 = re.sub("(\s*【.*$)|(^.*◥)|(\s+\w*$)", "", list_str)
    return rp_1

Doc = open('D:/YY.txt','r',encoding= 'utf8')
YY_List = PYQ(Doc.read())
Member_List = YY_List('span.name')

f = open('D:/YY_List.txt', 'w')
for i in Member_List:
    new_list = rpfun(PYQ(i).text())
    f.write(new_list+'\n')
f.close()

