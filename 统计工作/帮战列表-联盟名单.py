#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


def convert(str_line):
    # 空格换成制表符
    s1 = str_line.strip()
    s2 = re.sub(" ", "	", s1)
    return s2.split('	')[:2]


def get_num(file):
    with open(file, 'r', encoding='utf-8') as pre:
        lines = pre.readlines()
        for xl in range(len(lines)):
            mk1 = int(convert(lines[xl])[0])
            mk2 = int(convert(lines[xl-1])[0])
            if (mk1 > 1) & (mk2 == 1) & (xl < 200) & (xl != 1):
                return xl

File_list = ["1.txt", "2.txt", "3.txt", "4.txt"]
Con_list = ["Member_List_1.txt", "Member_List_2.txt", "Member_List_3.txt", "Member_List_4.txt"]

print("请务必确认当前目录下存在 1.txt 2.txt 3.txt 4.txt文件\n")


for x in [0, 1, 2, 3]:
    with open(File_list[x], 'r', encoding='utf-8') as Pre:
        lls = Pre.readlines()
        num = get_num(File_list[x])
        with open(Con_list[x], 'w', encoding='utf-8') as Con:
            for n in range(num-1):
                Con.write(convert(lls[n])[1]+'\n')