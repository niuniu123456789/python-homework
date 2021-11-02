#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：1901班 侯志青 29号
@Date    ：2021/10/3 21:11
题目：建立一个APP的使用频率排行榜，实现对排行榜的查询、更新操作
应用场景：对APP使用频率的用户查询及 更新(对指定元素进行更改，和增加元素)操作
"""

# 某年使用频率最高的APP排行（作业演示，本人虚构）
list = ['Taobao', 'Runoob', "Zhihu", "Google", "Wiki"]
print("打印APP的使用排行榜", list)

# 读取使用率最高的排行榜的第二位
print("APP使用频率排行榜第二位: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print("排行榜的[1:-2]位: ", list[1: -2])

# 用户更新的操作
print("进行更新排行榜操作")
print("目前的排行榜第三为 : ", list[2])
list[2] = "Pingduoduo"
print("更新后的第三个元素为 : ", list[2])

print("为排行榜增加元素")
list.append("Baidu")
print("更新后的列表 : ", list)