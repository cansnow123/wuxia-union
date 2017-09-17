import re


def rp_fun(list_str):
    rp_1 = re.sub("(\s*【.*$)|(^.*◥)|(\s+\w*$)|  ", "", list_str)
    return rp_1

New_List = []

with open('YY.txt', 'r', encoding='utf-8') as Y:
    for i in Y:
        New_List.append(i.strip())
with open('YY_Valid.txt', 'w', encoding='utf-8') as Z:
    for l in New_List:
        if rp_fun(l) != "":
            Z.write(rp_fun(l).strip()+'\n')
        else:
            pass
