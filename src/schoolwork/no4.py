#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/10/11 23:22
"""

# 1
def frequency():
    from collections import Counter
    text = input('请输入一个字符串：')
    frequencies = Counter(text)
    print(frequencies)
frequency()


# 2
def countOnce():
    text = input('请输入一个字符串：')
    positions = [(ch, index) for index, ch in enumerate(text) if text.index(ch) == text.rindex(ch)]
    print(positions)
countOnce()


# 3
def last():
    '''
    输入一个字符串,输出其中每个唯一字符最后一次出现的下标
    :return:
    '''
    input('请输入一个字符串：')
    dict1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
             'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
             'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
             'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    # 用于指示字符串的字符下标
    num = 0

    def function(a, dict1, num):
        for i in a:
            num += 1
            if i in dict1:
                dict1[i] = num
        return dict1

    a = str(input())
    function(a, dict1, num)
    for x in dict1:
        if dict1[x] != 0:
            print("char:{}, last site:{}".format(x, dict1[x]))
last()


# 4
def union():
    '''
    输入包含若干集合的列表，输出这些集合的并集
    '''
    from functools import reduce

    lstA = eval(input("请输入一个列表:"));
    print(reduce(lambda x, y: x | y, lstA));


union()


# 5
def encryption():
    '''
    输入一个字符串,输出加密后的结果字符串。加密规则为:每个字符的Unicode编码和下一个字符的Unicode编码相减,
    用这个差的绝对值作为Unicode编码,对应的字符作为当前位置上字符的加密结果,最后一个字符是和第一个字符进行运算
    :return:
    '''
    text = input('请输入一个字符串：')
    result = [chr(abs(ord(ch) - ord(text[index + 1]))) for index, ch in enumerate(text[:-1])]
    result.append(chr(abs(ord(text[-1]) - ord(text[0]))))
    print(result)

encryption()


# 6
def palindrome():
    str1 = input('请输入一个字符串')
    str2 = str1[::-1]
    if str1 == str2:
        print('Yes')
    else:
        print('No')

palindrome()

