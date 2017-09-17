import re


def cvl(line):
    # 删除消耗
    step1 = re.sub("\s*\d+\s*$", "", line)
    # 删除帮众名空白至帮派间空白()包括职位
    step2 = re.sub("\s*(龙首|长老|副龙首|无职位|特需官)\s*", "\t", step1)
    # 只保留获得
    step3 = re.sub("\s*\d+\s+(?=\d+$)", "\t", step2)
    return step3

with open("LianMeng_DKP.txt", 'r', encoding='utf-8') as LMD:
    lines = LMD.readlines()
    if "PVE" in lines[1]:
        with open("Converted_LianMeng_DKP_PVE.txt", 'w', encoding='utf-8') as LMDC:
            for l in lines:
                if "本周" in l or "PVE" in l or "PVP" in l:
                    pass
                elif "消耗" in l:
                    LMDC.write("帮众\t帮派\t获得\n")
                else:
                    LMDC.write(cvl(l)+"\n")
    elif "PVP" in lines[1]:
        with open("Converted_LianMeng_DKP_PVP.txt", 'w', encoding='utf-8') as LMDC:
            for l in lines:
                if "本周" in l or "PVE" in l or "PVP" in l:
                    pass
                elif "消耗" in l:
                    LMDC.write("帮众\t帮派\t获得\n")
                else:
                    LMDC.write(cvl(l)+"\n")
