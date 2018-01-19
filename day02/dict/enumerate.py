#!/usr/bin/env python
# -*- coding:utf-8 -*-

while   True:
    li = ["电脑","鼠标垫","U盘","游艇"]
    for key,item in enumerate(li):
         print(key,item)

    inp = input("请输入商品:")
    inp_num = int(inp)
    print("您的选择为：",li[inp_num])



