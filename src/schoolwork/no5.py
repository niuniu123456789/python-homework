#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/10/17 22:44
抱歉老师，音量较小，请将音量调节至 50 - 65
"""

#  第一题
def function(n, list1):
    for i in range(2, n):
        while i != n:
            if n % i == 0:
                list1.append(i)
                n = n/i
            else:
                break
    list1.append(int(n))
    return list1

n = int(input("请输入一个正整数："))
list1 = []
function(n, list1)
print(list1)

# 第二题
def n_a():
    '''
    接收两个正整数参数n和a（要求a小于10的自然数），计算形式入a+aa+aaa+...+aaa...aaa
    :return:
    '''
    n=int(input("输入正整数参数n："))
    a=int(input("输入正整数参数a(小于10)："))
    s=0
    list1=[0]
    for i in range(1,n+1):
        list1.append(list1[i-1]*10+a)
    list1.remove(0)
    print(list1)
    print(sum(list1))
n_a()


def last_num():
    '''
    模拟报数游戏。有n个人围成一圈，从O到n一1按顺序编号，从第一个人开始从1到k报数，报到k的人退出圈子，然后圈子缩小，
    从下一个人继续游戏，问最后留下的是原来的第几号
    :return:
    '''
    n = int(input('请输入人数：'))
    k = int(input('请输入从第几个人开始报数：'))
    c = []
    for i in range(1, n + 1):
        c.append(i)
    num = 1
    while len(c) != 1:
        c.append(c.pop(0))  # 把已报数的人取出放到队尾，以此实现围成圈循环往复
        num += 1
        if num == k:
            del c[0]  # 把报到规定数字的人踢出圈子
            num = 1  # 重新从1开始报数
    print('输出最后留下人的号码：%s' % c)
last_num()

def baoshu():
    '''
    接收一个字符串作为参数，判断该参数是否为回文（正读和反读都一样的字符串），
    如果是则返回True,否则返回False。不允许使用切片。
    :return:
    '''
    str1=input("接收一个字符串（判断其是否为回文）：")
    n=len(str1)
    str2=[]
    for i in range(0,n):
        str2.append(str1[n-i-1])    #str2是列表
    if list(str1)==str2:            #将str1的字符形态转为列表
        return print("True")
    else:               # 正读和反读不一样的字符串
        return print("False")
baoshu()
