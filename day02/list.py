#!/usr/bin/env python
# -*- coding:utf-8 -*-

names = ["ZhangYang","GuYun","XiangPeng","XuLiangChen"]
#print(names)
print(names[0])
if names[0] == "ZhangYang":
    print("True")
else:
    print("False")



while True:
    salary = input("请输入你的金额:")
    if salary.isdigit():
        salary = int(salary)
        exit()
    else:
        print("你输入的不是数字")

