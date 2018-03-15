#!/usr/bin/env python
# -*- coding:utf-8 -*-
num = "alex"
li = ['alex', 'eirc']
if num in li:
    print("在")
else:
    print("不在")

if num in li and num.startswith('a'):
    print("在")
else:
    print("不在")