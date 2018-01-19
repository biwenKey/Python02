#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"jinbiwen",
    "age":27,
    "shengao":170,
    "dizhi":"青浦区，罗家四队"
}

ret = 'wocao' in user_info.keys()
#print("age"in user_info.keys())
if ret == True:
    print("this is a True")
else:
    print("wocao,this is False")

