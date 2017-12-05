#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
product_list = [
    ("Iphone",5800),
    ("Mac Pro",9800),
    ("Bike",800),
    ("Watch",100600),
    ("Coffee",31),
    ("Alex Python",120)
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("请选择你要购买的产品的编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
        elif user_choice == "q":
            print("------------shopping list--------------")
            for p in shopping_list:
                print(p)
            print("your current balance:",salary)
            exit()
        else:
            print("invalid option")
            time.sleep(4)
            print("请你再次输入你要购买的商品的编号：")
            time.sleep(1)


