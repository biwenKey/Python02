#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
cmd_res = os.system("dir")
print(cmd_res)
cmd_res02 = os.popen("dir")
print(cmd_res02)
print("this is test")


