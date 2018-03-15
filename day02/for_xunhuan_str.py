
#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = "alex hello"
for i in s:
    if i == "l":
        continue
    print(i)

for i in s:
    if i  == "l":
        break
    print(i)

