#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "alex is shabi"
start = 0
while start < len(s):
    name = s[start]
    if start == 2:
        continue
    print(name)
    start +=1
