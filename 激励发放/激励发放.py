import re
import os

FL = ["_1.txt", "_2.txt", "_3.txt", "_4.txt"]
FL_Sub_1 = ["BangPai_DKPFaFangJiLi_G1.txt", "BangPai_DKPFaFangJiLi_S1.txt"]
FL_Sub_2 = ["BangPai_DKPFaFangJiLi_G2.txt", "BangPai_DKPFaFangJiLi_S2.txt"]
FL_Sub_3 = ["BangPai_DKPFaFangJiLi_G3.txt", "BangPai_DKPFaFangJiLi_S3.txt"]
FL_Sub_4 = ["BangPai_DKPFaFangJiLi_G4.txt", "BangPai_DKPFaFangJiLi_S4.txt"]
# EXCEL内容--数组格式
BP_1 = []
BP_2 = []
BP_3 = []
BP_4 = []
sample = "发放激励\n领取情况        	帮众                      	等级              	职位                  	剩余PVP-DKP       	修改PVP-DKP       	剩余PVE-DKP       	修改PVE-DKP       	发放数量        \n"

# 激励箱子发放文件初始化
with open("BangPai_DKPFaFangJiLi_G1.txt", 'w', encoding='utf-8') as initf_g, open("BangPai_DKPFaFangJiLi_S1.txt", 'w', encoding='utf-8') as initf_s:
        initf_g.write(sample)
        initf_s.write(sample)
with open("BangPai_DKPFaFangJiLi_G2.txt", 'w', encoding='utf-8') as initf_g, open("BangPai_DKPFaFangJiLi_S2.txt", 'w', encoding='utf-8') as initf_s:
    initf_g.write(sample)
    initf_s.write(sample)
with open("BangPai_DKPFaFangJiLi_G3.txt", 'w', encoding='utf-8') as initf_g, open("BangPai_DKPFaFangJiLi_S3.txt", 'w', encoding='utf-8') as initf_s:
    initf_g.write(sample)
    initf_s.write(sample)
with open("BangPai_DKPFaFangJiLi_G4.txt", 'w', encoding='utf-8') as initf_g, open("BangPai_DKPFaFangJiLi_S4.txt", 'w', encoding='utf-8') as initf_s:
    initf_g.write(sample)
    initf_s.write(sample)
# 文件初始化结束

# 加载文件，将EXCEL格式内容转换为数组格式
with open(FL[0], 'r', encoding='utf-8') as bp1:
    for lines in bp1:
        BP_1.append(lines.split("	"))
with open(FL[1], 'r', encoding='utf-8') as bp2:
    for lines in bp2:
        BP_2.append(lines.split("	"))
with open(FL[2], 'r', encoding='utf-8') as bp3:
    for lines in bp3:
        BP_3.append(lines.split("	"))
with open(FL[3], 'r', encoding='utf-8') as bp4:
    for lines in bp4:
        BP_4.append(lines.split("	"))
# 结束转换

# 激励文件自动化文件部署
# BP_1[x][5]对应EXCEL中    发放
# BP_1[x][0]对应EXCEL中    ID
for x in range(len(BP_1)):
    # 银箱子
    if float(BP_1[x][5]) > 0:
        with open(FL_Sub_1[1], 'a', encoding='utf-8') as fl1_1:
            fl1_1.write("8/8	"+BP_1[x][0]+"	90	X	0	0	0	0	8"+"\n")
    # 金箱子
    if BP_1[x][5] == '1':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_1:
            fl1_1.write("1/6	"+BP_1[x][0]+"	90	X	0	0	0	0	1"+"\n")
    if BP_1[x][5] == '2':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_2:
            fl1_2.write("2/6	"+BP_1[x][0]+"	90	X	0	0	0	0	2"+"\n")
    if BP_1[x][5] == '3':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_3:
            fl1_3.write("3/6	"+BP_1[x][0]+"	90	X	0	0	0	0	3"+"\n")
    if BP_1[x][5] == '4':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_4:
            fl1_4.write("4/6	"+BP_1[x][0]+"	90	X	0	0	0	0	4"+"\n")
    if BP_1[x][5] == '5':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_5:
            fl1_5.write("5/6	"+BP_1[x][0]+"	90	X	0	0	0	0	5"+"\n")
    if BP_1[x][5] == '6':
        with open(FL_Sub_1[0], 'a', encoding='utf-8') as fl1_6:
            fl1_6.write("6/6	"+BP_1[x][0]+"	90	X	0	0	0	0	6"+"\n")

for x in range(len(BP_2)):
    # 银箱子
    if float(BP_2[x][5]) > 0:
        with open(FL_Sub_2[1], 'a', encoding='utf-8') as fl1_1:
            fl1_1.write("8/8	" + BP_2[x][0] + "	90	X	0	0	0	0	8" + "\n")
    # 金箱子
    if BP_2[x][5] == '1':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_1:
            fl2_1.write("1/6	"+BP_2[x][0]+"	90	X	0	0	0	0	1"+"\n")
    if BP_2[x][5] == '2':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_2:
            fl2_2.write("2/6	"+BP_2[x][0]+"	90	X	0	0	0	0	2"+"\n")
    if BP_2[x][5] == '3':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_3:
            fl2_3.write("3/6	"+BP_2[x][0]+"	90	X	0	0	0	0	3"+"\n")
    if BP_2[x][5] == '4':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_4:
            fl2_4.write("4/6	"+BP_2[x][0]+"	90	X	0	0	0	0	4"+"\n")
    if BP_2[x][5] == '5':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_5:
            fl2_5.write("5/6	"+BP_2[x][0]+"	90	X	0	0	0	0	5"+"\n")
    if BP_2[x][5] == '6':
        with open(FL_Sub_2[0], 'a', encoding='utf-8') as fl2_6:
            fl2_6.write("6/6	"+BP_2[x][0]+"	90	X	0	0	0	0	6"+"\n")

for x in range(len(BP_3)):
    # 银箱子
    if float(BP_3[x][5]) > 0:
        with open(FL_Sub_3[1], 'a', encoding='utf-8') as fl1_1:
            fl1_1.write("8/8	" + BP_3[x][0] + "	90	X	0	0	0	0	8" + "\n")
    # 金箱子
    if BP_3[x][5] == '1':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_1:
            fl3_1.write("1/6	"+BP_3[x][0]+"	90	X	0	0	0	0	1"+"\n")
    if BP_3[x][5] == '2':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_2:
            fl3_2.write("2/6	"+BP_3[x][0]+"	90	X	0	0	0	0	2"+"\n")
    if BP_3[x][5] == '3':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_3:
            fl3_3.write("3/6	"+BP_3[x][0]+"	90	X	0	0	0	0	3"+"\n")
    if BP_3[x][5] == '4':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_4:
            fl3_4.write("4/6	"+BP_3[x][0]+"	90	X	0	0	0	0	4"+"\n")
    if BP_3[x][5] == '5':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_5:
            fl3_5.write("5/6	"+BP_3[x][0]+"	90	X	0	0	0	0	5"+"\n")
    if BP_3[x][5] == '6':
        with open(FL_Sub_3[0], 'a', encoding='utf-8') as fl3_6:
            fl3_6.write("6/6	"+BP_3[x][0]+"	90	X	0	0	0	0	6"+"\n")

for x in range(len(BP_4)):
    # 银箱子
    if float(BP_4[x][5]) > 0:
        with open(FL_Sub_4[1], 'a', encoding='utf-8') as fl1_1:
            fl1_1.write("8/8	" + BP_4[x][0] + "	90	X	0	0	0	0	8" + "\n")
    # 金箱子
    if BP_4[x][5] == '1':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_1:
            fl4_1.write("1/6	"+BP_4[x][0]+"	90	X	0	0	0	0	1"+"\n")
    if BP_4[x][5] == '2':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_2:
            fl4_2.write("2/6	"+BP_4[x][0]+"	90	X	0	0	0	0	2"+"\n")
    if BP_4[x][5] == '3':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_3:
            fl4_3.write("3/6	"+BP_4[x][0]+"	90	X	0	0	0	0	3"+"\n")
    if BP_4[x][5] == '4':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_4:
            fl4_4.write("4/6	"+BP_4[x][0]+"	90	X	0	0	0	0	4"+"\n")
    if BP_4[x][5] == '5':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_5:
            fl4_5.write("5/6	"+BP_4[x][0]+"	90	X	0	0	0	0	5"+"\n")
    if BP_4[x][5] == '6':
        with open(FL_Sub_4[0], 'a', encoding='utf-8') as fl4_6:
            fl4_6.write("6/6	"+BP_4[x][0]+"	90	X	0	0	0	0	6"+"\n")
