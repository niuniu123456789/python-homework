#!/usr/bin/env python
# coding: UTF-8
'''
@author lvy
@date 2021/5/18 21:29
'''

str1 = "abc"
int1 = 123
float1 = 123.123
bool1 = True

#创建数据容器
list1 = [str1,int1,float1,bool1]
set1 = {str1,int1,float1,bool1}
dict1 = {'str':str1,'int':int1,'float':float1}

#打印、查看数据容器
print(list1)
print(set1)
print(dict1)

print(type(list1))
print(type(set1))
print(type(dict1))

#转换 数据容器类型
print("---------------------------")
print(int(float1))          #基础数据类型转化
print(type(int(float1)))

print(set(list1))
print(type(set(list1)))
print(list(set(list1)))

#查找数据、更新、删除
print("---------------------------")
print(list1)
print(list1[2])

# print(set1[2])  集合不支持index
print(list1)
print(list(set1)[2])
# print(dict1[2])  ['key']
print(dict1)
print(dict1['str'])

#更新
print(list1)
print(list1.append("append"))
print(list1.remove("append"))




