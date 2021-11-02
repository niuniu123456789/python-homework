#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：软工1901 侯志青 29号
@Date    ：2021/10/4 20:38
"""
# 第1题
def average():
    s = eval(input("1.请输入自然数列表："))
    sum = 0
    for i in s:
        sum += i
    avg = sum/len(s)
    print('%.3f'%avg)

average()

# 第2题
def descending():
    s = eval(input("2.降序，请输入自然数列表："))
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if s[i] < s[j]:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
    print(s)

descending()

# 第3题
def digits():
    s = eval(input("3.自然数的位数的题目，请输入自然数列表："))
    m = []
    n = 0
    for i in s:
        m.append(len(str(i)))
        n+=1
    print(m)

digits()

# 第4题
def max_abs():
    s = eval(input("4.求绝对值最大值的题目，请输入整数列表："))
    max = s[0]
    for i in s:
        if abs(max) < abs(i):
            max =i
    print(max)

max_abs()

# 第5题
def multiplication():
    s = eval(input("5.求乘积的题目，请输入整数列表："))
    p = s[0]
    for i in s:
        p = p * i
    #     要求输出整形， 除法可能输出小数，所以设置一个强转
    p = int(p/s[0])[2,3]
    print(p)

multiplication()

# 第6题
def vector():
    # 因为需要 用户输入两个序列，所以需要两次输入
    input("6.求两个向量内积积的题目(该句话不需要输入)")
    s1 = eval(input("请输入第一个整数列表："))
    s2 = eval(input("请输入第二个等长整数列表："))
    m = []
    # range(0,len(s2))也可以
    for i in range(0,len(s1)):
        m.append(s1[i] * s2[i])
    print(m)

vector()