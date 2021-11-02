#!/usr/bin/env python
# coding: UTF-8
'''
@author lvy
@date 2021/5/29 15:26
'''

# while 执行判断咖啡浓度是否达到标准，如果没有达到，就继续倒入咖啡粉
coffee = 10
coffee_standard = 20
each_time = 3

# while 咖啡浓度 < 标准浓度 :
#     继续加咖啡粉

while coffee < coffee_standard:
    print("----------------------------")
    print("继续加咖啡粉", each_time, 'g')
    print("未加入咖啡粉，当前咖啡粉含量：", coffee)
    coffee = coffee + each_time
    print("已加入咖啡粉，当前咖啡粉含量：", coffee)

# for 遍历销售列表中的数据，并对所有数据进行累加（求和）
#     for 销售列表中的数据项
#         累加数据项
    sales = [123,234,345,567]
    sum_sales = 0 #0.00

    for sale in sales:  #sale，也可以是aaa.asd等
        print("当前数据项",sale)
        sum_sales = sum_sales + sale
    print(sum_sales)