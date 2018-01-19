#!/usr/bin/env python
# -*- coding:utf-8 -*-
#让enumerate默认从1开始:
li = ["电脑","鼠标垫","U盘","游艇"]
for key,item in enumerate(li,1):
    print(key,item)

#inp = input("请输入商品:")
#inp_num = int(inp)
#print(li[inp_num - 1])

#根据元素找索引
inp = input("请输入内容:")
ret = li.index(inp)
print(ret)

