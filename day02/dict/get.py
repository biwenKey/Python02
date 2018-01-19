#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"jinbiwen",
    "age":27,
    "shengao":170,
    "dizhi":"青浦区，罗家四队"
}

print(user_info)
val = user_info.get("age1111")
print(val)
print(user_info["name"])
#print(user_info["age111"])
val02 = user_info.get("age111",123)
print(val02)