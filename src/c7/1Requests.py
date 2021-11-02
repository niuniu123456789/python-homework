#!/usr/bin/env python
# coding: UTF-8
'''
@Author  ：lvy
@Date    ：2021/5/30 16:40
'''

#导入模块
import requests

#定义url
url_douban_movie = "https://movie.douban.com/"
#headers
headers = {'user-agent': 'my-app/0.0.1'}

#-----------------------------------------------
# #访问、并获取网页信息
# #response 响应 requests 请求
# response_douban_movie = requests.get(url=url_douban_movie,headers = headers)
#
# print(response_douban_movie.text)
#
# ## XX电影主页
# # ?tag=%E7%83%AD%E9%97%A8&from=gaia  为参数，用来标记信息。可以舍去
# url2 = "https://movie.douban.com/subject/35296028/"
# response2 = requests.get(url=url2,headers = headers)
# print(response2.text)

##百度百科
url3 = "https://baike.baidu.com"
response3 = requests.get(url=url3,headers = headers)
print(response3.text)