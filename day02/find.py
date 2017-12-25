#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = "alex hello"
print(s.find('ex'))
print(s.index('ex'))
print(s[2])
print(s[0:2])
print(len(s))
print(s[0:10])
for i in s:
    print(i)
start = 0
while start < len(s):
    temp = s[start]
    if temp == 'l':
        continue
    print(s[start])
    start += 1

