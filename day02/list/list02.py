#!/usr/bin/env python
# -*- coding:utf-8 -*-
name_list = ["eirc","alex","tony"]
##追加
name_list.append('seven')
print(name_list)
print(name_list[len(name_list)- 1])
##记数
name_list.append('seven')
name_list.append('seven')
print(name_list)
print(name_list.count('seven'))
##扩展
temp = [11,22,33,44]
name_list.extend(temp)
print(name_list)
##获取某个值的索引
print(name_list.index(11))
print(name_list[6])
del name_list[6]
print(name_list)
print(len(name_list))
del name_list[6:9]
print(name_list)
##往 某个索引的位置插入值
name_list.insert(0,'SB')
print(name_list)

