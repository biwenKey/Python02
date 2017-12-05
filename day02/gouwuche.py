#!/usr/bin/env python
# -*- coding:utf-8 -*-

wages = int(input("please input your wages:"))
#print(type(wages))

print("商品列表如下：")
shangping = [[1,"笔记本",4000],[2,"手机",1800],[3,"耳机",200]]
print(shangping)
bianhao = int(input("请输入你要购买的商品编号："))
#print(type(bianhao))
#print(type(shangping[0][0]))
if bianhao == shangping[0][0]:
    if wages < shangping[0][2]:
        print("您购买的1号商品余额不足")
    else:
        print("恭喜你购买笔记本成功")
if bianhao == shangping[1][0]:
    if wages < shangping[1][2]:
            print("您购买2号商品手机余额不足")
    else:
        print("恭喜你购买手机成功")
if bianhao == shangping[2][0]:
    if wages < shangping[2][2]:
        print("您购买的3号上平余额不足")
    else:
        print("恭喜您购买商品耳机成功")







