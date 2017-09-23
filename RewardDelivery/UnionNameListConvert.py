import re


def cvl(line):
    # 删除消耗
    step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名空白至帮派间空白()包括职位
    step2 = re.sub("\s*(龙首|长老|副龙首|无职位|特需官)\s*", "\t", step1)
    return step2


UnionNameList = []
with open("LianMeng_DKP.txt", 'r', encoding='utf-8') as LMD:
    for l in LMD.readlines():
        if "本周" in l or "PVE" in l or "PVP" in l:
            pass
        elif "消耗" in l:
            pass
        else:
            UnionNameList.append(cvl(l).split('\t'))

print(UnionNameList)
