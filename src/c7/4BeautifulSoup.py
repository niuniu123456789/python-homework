#!/usr/bin/env python
# coding: UTF-8
'''
@Author  ：lvy
@Date    ：2021/5/30 19:42
'''

from bs4 import BeautifulSoup
import requests
import re

#获取网页全部信息

#定义url
url_douban_movie = "https://m.douban.com/movie/subject/1292064/"
#headers
headers = {'user-agent': 'my-app/0.0.1'}
#访问、并获取网页信息
#response 响应 requests 请求
response = requests.get(url=url_douban_movie,headers = headers)
print(response.text)

print("\n-----------------------\n")



#解析网页
soup = BeautifulSoup(response.text, 'html.parser')  #response返回的为：实体       response.text返回值：长度
#之后，美化网页
print(soup.prettify())

#-----------------------------------------------
# 提取目标信息
print(soup.title.string)   # .获得属性     #标题
# 提取以b开头的标签
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# 提取class标签，find与find_all的区别
# css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]
print(soup.find("div",class_ = 'bd').text)

#[]代表是队列，用[坐标即数字]来定位

