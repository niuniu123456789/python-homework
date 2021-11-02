#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/10/4 21:49
"""
import os
from idlelib.iomenu import encoding

# path = r"C:\Users\asus\Desktop\PythonPro07\Pro0701.txt"
# sys.setdefaultencoding('utf-8')
# f = (path,'r',)
# print(f.read())

with open("infomation.txt", encoding="utf") as f3:
    f3.seek(300)
    print(f3.read(50))
    f3.seek(900)
    print(f3.read(50))