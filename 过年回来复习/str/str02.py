#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "jinbiwen"
ret = s.capitalize()
print(ret)
print(s.capitalize())

a1 = "alex"
ret = a1.center(6, '*')
print(ret)

a2 = "alex is alph"
ret = a2.count('a')
print(ret)
ret01 = a2.count('al')
print(ret01)
ret02 = a2.count('al', 0,10)
print(ret02)