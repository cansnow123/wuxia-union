#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

AF = os.popen('tree /A /F').readlines()
mark = 0
for x in range(len(AF)):
    if AF[x] == '+---OLD\n':
        mark = x

TL = AF[2:mark]

with open('Tree_List.txt','w', encoding='utf-8') as N:
    for x in TL:
        N.write(x)





