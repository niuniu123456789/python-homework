#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/10/17 23:16
cycle()
函数仅接受一个参数作为输入，可以像列表，字符串，元组等
该函数返回迭代器对象类型
# cycle('ABCD') --> A B C D A B C D A B C D ...
"""
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
cycle("ABCD")