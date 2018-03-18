#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州": ["不知道", "少林寺", "嵩山"],
        "开封": ["包拯", "展昭", "威士忌"],
    },
    "山西": {
        "太原": ["xxx", "ooo", "小店"],
        "运城": ["更不知道了", "999", "哈尔冰啤酒"],
    },
 }

for a in dic:
    print(a)
news01 = input("请输入以上的随便一个省份:")
b = dic[news01]
for c in b:
    print(c)
news02 = input("请输入以上的随便一个市:")
d = dic[news01][news02]
#print(d)
for e in d:
    print(e)