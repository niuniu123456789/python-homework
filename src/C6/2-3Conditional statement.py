#!/usr/bin/env python
# coding: UTF-8
'''
@author lvy
@date 2021/5/21 21:34
'''
coffee_max = 10 #  上限 ，太浓了
coffee_min = 5  #  下限 ，太淡了
coffee = 7#   当前浓度

# if 咖啡浓度正好:
#     执行：倒牛奶
# elif 咖啡浓度太浓：
#     执行：倒水
# else:
#     执行：加咖啡粉的操作

print("当前咖啡粉浓度为："coffee)
# if coffee < 10 and coffee <5:

if coffee < coffee_max and coffee > coffee_min:
    print("咖啡浓度正好，继续倒牛奶")
elif coffee > coffee_max:
    print("咖啡浓度太浓，继续倒倒水")
else:
    print("咖啡浓度太淡，继续倒咖啡粉")

