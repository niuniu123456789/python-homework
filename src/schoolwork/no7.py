#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/10/22 21:41
视频音量 26-35可以听清
"""
# 生成器的生成
def add():
    for i in range(10):
        yield i
g = add()
print(g)  # <generator object add at 0x10f6110f8>
print(next(g))  # 0
print(next(g))  # 1


def gen():
    print('111111')
    yield '111111'
    print('222222')
    yield '222222'
    print('333333')
    yield '333333'
g = gen()
print(g)  # <generator object gen at 0x0026BBF0>
next(g)   # 111111
next(g)   # 222222
next(g)   # 333333
next(g, 'over')

# 生成器函数使用场景
# 死循环
def way():
    i = 0
    while True:
        i += 1
        yield i # 1，2，3
c = way()

# 在生成器函数中使用死循环，不会一直执行，依旧是执行多少次next(),返回多少个值
print(next(c)) # 1
print(next(c)) # 2
print(next(c)) # 3
print(next(c)) # 4
print(next(c)) # 5
