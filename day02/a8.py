#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = "alex SB alex"
print(s.partition('SB'))
s02 = "alex SB alex SB alex"
print(s02)
ret = s02.replace("al","GG",3)
print(ret)
print(s02.find('x'))
print(s02.rfind('x'))
print(len(s02))
print(s02.index('x'))

print(s02.rindex('a'))
s03 = "this is test"
print(s03.rjust(20,'x'))

s04 = "women doushi zhongguoren"
print(s04.rpartition("doushi"))



