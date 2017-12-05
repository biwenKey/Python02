#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy
names = ["4ZhangYang","#!GuYun","xXiangPeng",["alex","jack"],"ChenRonghua","XuLiangChen"]
name2 =  copy.deepcopy(names)
names[2] = "向鹏"
names[3][0] = "ALEXANDER"

print(names)
print(name2)
for i in name2:
    print(i)

