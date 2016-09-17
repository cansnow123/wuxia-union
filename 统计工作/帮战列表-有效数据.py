#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os


def convert(str_line):
    # 删除行首数字
    s1 = re.sub("^^\d+ ", "", str_line)
    # 删除0战绩
    s2 = re.sub("^.*\s0 0 0", "", s1)
    # 删除职业
    s3 = re.sub(" 天香| 太白| 五毒| 神威| 真武| 丐帮| 唐门| 神刀", "", s2)
    s4 = re.sub("\s*$", "", s3)
    # 空格换成制表符
    s5 = re.sub(" ", "	", s4)
    # 空行处理最终保留数据依次为 ID、荣誉数、击杀、助攻
    return s5

File_list = ["1.txt", "2.txt", "3.txt", "4.txt"]
Con_list = ["Converted_1.txt", "Converted_2.txt", "Converted_3.txt", "Converted_4.txt"]

if os.path.exists("1.txt") or os.path.exists("2.txt") or os.path.exists("3.txt") or os.path.exists("4.txt"):
    print("请确认当前目录下存在 1.txt 2.txt 3.txt 4.txt文件\n")
    input("")
    exit()

for x in [0, 1, 2, 3]:
    with open(File_list[x], 'r', encoding='utf-8') as Pre:
        with open(Con_list[x], 'w', encoding='utf-8') as Con:
            for i in Pre:
                if convert(i) != "":
                    Con.write(convert(i)+'\n')
                else:
                    pass

Con_list = ["Converted_1.txt", "Converted_2.txt", "Converted_3.txt", "Converted_4.txt"]
Union1_list = []
Union2_list = []
Union3_list = []
Union4_list = []

with open(Con_list[0], 'r', encoding='utf-8') as Pre:
    for y in Pre:
        Union1_list.append(y.strip().split("	"))

with open(Con_list[1], 'r', encoding='utf-8') as Pre:
    for y in Pre:
        Union2_list.append(y.strip().split("	"))

with open(Con_list[2], 'r', encoding='utf-8') as Pre:
    for y in Pre:
        Union3_list.append(y.strip().split("	"))

with open(Con_list[3], 'r', encoding='utf-8') as Pre:
    for y in Pre:
        Union4_list.append(y.strip().split("	"))


def list_process(union_list):
    id_list = []
    x1 = len(union_list)
    for n in range(x1):
        id_list.append(union_list[n][0])

    # 筛选不重复的ID列表(透视时使用的名单)
    al_id_list = sorted(set(id_list), key=id_list.index)
    x2 = len(al_id_list)

    # 转换为多维
    mk_list = [[l, []] for l in al_id_list]
    # mk_list记录了ID以及重复的元素下标用于后一步统计如[['楪夢', 0, 9, 19], ['凌渃尘', 1, 10, 18],...]
    for n in range(x2):
        for m in range(x1):
            if id_list[m] == al_id_list[n]:
                mk_list[n][1].append(m)

    # st_list用作最终的透明表数据(一样首先转换为多维)
    st_list = [[l] for l in al_id_list]
    _honor = 0
    _kill = 0
    _ass = 0

    for n in range(len(st_list)):
        for m in range(len(mk_list[n][1])):
            _honor += int(union_list[mk_list[n][1][m]][1])
            _kill += int(union_list[mk_list[n][1][m]][2])
            _ass += int(union_list[mk_list[n][1][m]][3])
        st_list[n].append([_honor, _kill, _ass])
        _honor = 0
        _kill = 0
        _ass = 0

    print("转换过程：")
    print(union_list)
    print("↓↓↓↓")
    print(al_id_list)
    print("↓↓↓↓")
    print(mk_list)
    print("↓↓↓↓")
    print(st_list)
    return st_list


with open("Final-1.txt", 'w', encoding='utf-8') as f:
    w = list_process(Union1_list)
    for st in w:
        f.write(str(st[0]) + "	" + str(st[1][0]) + "	" + str(st[1][1]) + "	" + str(st[1][2]) + "\n")
os.remove("Converted_1.txt")

with open("Final-2.txt", 'w', encoding='utf-8') as f:
    w = list_process(Union2_list)
    for st in w:
        f.write(str(st[0]) + "	" + str(st[1][0]) + "	" + str(st[1][1]) + "	" + str(st[1][2]) + "\n")
os.remove("Converted_2.txt")

with open("Final-3.txt", 'w', encoding='utf-8') as f:
    w = list_process(Union3_list)
    for st in w:
        f.write(str(st[0]) + "	" + str(st[1][0]) + "	" + str(st[1][1]) + "	" + str(st[1][2]) + "\n")
os.remove("Converted_3.txt")

with open("Final-4.txt", 'w', encoding='utf-8') as f:
    w = list_process(Union4_list)
    for st in w:
        f.write(str(st[0]) + "	" + str(st[1][0]) + "	" + str(st[1][1]) + "	" + str(st[1][2]) + "\n")
os.remove("Converted_4.txt")