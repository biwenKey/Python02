#!/usr/bin/env python
# -*- coding:utf-8 -*-
while True:
    salary = input("请输入你的金额:")
    if salary.isdigit():
        salary = int(salary)
        exit()
    else:
        print("你输入的不是数字")
