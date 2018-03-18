#!/usr/bin/env python
# -*- coding:utf-8 -*-
#li = ["alec", " aric", "Alex", "Tony", "rain"]
li = ["aleb", " aric", "Alec", "Tony", "rain"]
new_list = []
for i in li:
#    print(i)
    news = i.strip()
   # print(news)
   # if news.startswith('a') or news.startswith('A') and news.endswith('c'):
    #    print(i)

    if (news.startswith('a') or news.startswith('A')) and  news.endswith('c'):
        new_list.append(news)
        print(new_list)

