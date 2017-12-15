#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getpass
_username = "alex"
_password = '123'
user  = input("请输出涌入户名:")
pwd  = input("请输入密码:")

if user == _username and pwd == _password:
    print("恭喜你登录成功!!!")
else:
    print("很遗憾，你登录失败了")
