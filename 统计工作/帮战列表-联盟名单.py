#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os


def convert(str_line):
    # 删除行首数字
    s1 = re.sub("^^\d+ ", "", str_line)
    # 删除0战绩
    s2 = re.sub(" \d+ \d+ \d+", "", s1)
    # 删除职业
    s3 = re.sub(" 天香| 太白| 五毒| 神威| 真武| 丐帮| 唐门| 神刀", "", s2)
    s4 = re.sub("\s*$", "", s3)
    # 空格换成制表符
    s5 = re.sub(" ", "	", s4)
    # 空行处理最终保留数据依次为 ID、荣誉数、击杀、助攻
    return s5

File_list = ["1.txt", "2.txt", "3.txt", "4.txt"]
Con_list = ["Member_List_1.txt", "Member_List_2.txt", "Member_List_3.txt", "Member_List_4.txt"]

if os.path.exists("1.txt") or os.path.exists("2.txt") or os.path.exists("3.txt") or os.path.exists("4.txt"):
    print("请确认当前目录下存在 1.txt 2.txt 3.txt 4.txt文件\n")
    input("")
    exit()

for x in [0, 1, 2, 3]:
    with open(File_list[x], 'r', encoding='utf-8') as Pre:
        with open(Con_list[x], 'w', encoding='utf-8') as Con:
            jud = Pre.readlines()
            if len(jud) > 152:
                for n in range(len(jud)):
                    if (jud[n][0:4] == jud[0][0:4]) & (n > 0 & n<300):
                        mk_st = n
                for m in range(mk_st):
                    Con.write(convert(jud[m])+'\n')
            else:
                for i in Pre:
                    Con.write(convert(i)+'\n')
