#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"jinbiwen",
    "age":27,
    "shengao":170,
    "dizhi":"青浦区，罗家四队"
}
#user_info.pop("name","shengao")
#print(user_info)
#user_info.pop("name")
#print(user_info)
print(user_info.popitem())
print(user_info.setdefault("wocao"))




