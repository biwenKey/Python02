#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"jinbiwen",
    "age":27,
    "shengao":170,
    "dizhi":"青浦区，罗家四队"
}
g = input("plaes input your chaxun:")
val = g in user_info.keys()

if val == True:
    print("this is a True")
else:
    print("this is a Fase")


