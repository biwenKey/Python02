#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"jinbiwen",
    "age":27,
    "shengao":170,
    "dizhi":"青浦区，罗家四队"
}
print(user_info)
test = {
    "a1":12,
    "a2":456
}
user_info.update(test)
print(user_info)
del user_info['a1']
print(user_info)
