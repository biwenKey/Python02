#!/usr/bin/env python
# -*- coding:utf-8 -*-
name = "李露"
for i in name:
    print(i)

bytes_list = (bytes(name,encoding='utf-8'))
print(bytes_list)
str_list = (str(bytes_list,encoding='utf-8'))
print(str_list)
for i in bytes_list:
    print(i)


