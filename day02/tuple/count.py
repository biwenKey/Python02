#!/usr/bin/env python
# -*- coding:utf-8 -*-
name_tuple = ("jinbiwen","wocao","hello","ai","ai","ai")
for i in name_tuple:
    print(i)


print(name_tuple.count("jinbiwen"))
print(name_tuple.count("ai"))
print(name_tuple.index("hello"))
print(len(name_tuple))
print(name_tuple[0:len(name_tuple)-1])
