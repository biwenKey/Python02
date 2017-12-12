#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = "123"
#它的本质上会去做一件什么事情？
#a = init => __init__(123)
#int.__init__()

a1 = int(123)
print(type(a))
print(type(a1))
a2 = int("0b100",2)
print(a2)
