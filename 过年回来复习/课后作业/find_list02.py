#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = ["aleb", " aric", "Alec", "Tony", "rain"]
new_list = []
for i in li:
    news = i.strip()
    if (news.startswith('a') or news.startswith('A')) and  news.endswith('c'):
    #if news.startswith('a') or news.startswith('A') and news.endswith('c'):
        new_list.append(news)
print(new_list)
