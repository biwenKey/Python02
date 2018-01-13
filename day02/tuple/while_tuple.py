#!/usr/bin/env python
# -*- coding:utf-8 -*-
name_tuple = ("sidalin","maozedong","jinbiwen")
i = 0
#print(len(name_tuple))
#print(name_tuple[2])
while i < len(name_tuple):
    t = name_tuple[i]
    if i == 2:
        continue
    print(t)
    i=i+1

print(name_tuple)
