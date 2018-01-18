#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_info = {
    "name":"alex",
    "age":73,
    "gender":'M'
}
print(user_info.keys())
print(user_info.values())
#获取字典中的所有键值对
print(user_info.items())
for i in user_info.keys():
    print(i)

for i in user_info.values():
    print(i)

for i in user_info.items():
    print(i)


for k,v in user_info.items():
    print(k,":",v)

user_info.clear()
print(user_info)