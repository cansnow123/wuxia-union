#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

a = os.popen('tree /A /F').readlines()
for x in range(len(a)):
    if a[x] == '+---OLD\n':
        mark = x

TL = a[2:mark]

with open('Tree_List.txt','w', encoding='utf-8') as N:
    for x in TL:
        N.write(x)