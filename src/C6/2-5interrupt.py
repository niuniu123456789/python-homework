#!/usr/bin/env python
# coding: UTF-8
'''
@Author  ：lvy
@Date    ：2021/5/29 21:52
'''
coffee = 10
coffee_standard = 20
each_time = 3
x = 1 #从第一杯咖啡开始卖
guest = 'li'#不卖，黑名单

#来人买咖啡/卖咖啡：<=25就正常卖   >25,就不卖
while True:
    if guest == 'Mike':
        print(guest)
        continue
        print('continue')

    print("目前已经做了", x, "杯")
  #制作咖啡
    while coffee < coffee_standard:
        print("\n----------------------------")
        print("继续加咖啡粉", each_time, "g")
        print("未加入咖啡粉，当前咖啡粉含量：", coffee)
        coffee = coffee + each_time
        print("已加入咖啡粉，当前咖啡粉含量：", coffee)
    if x < 25:
        x += 1
    else:
        break;