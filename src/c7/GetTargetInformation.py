#!/usr/bin/env python
# coding: UTF-8
"""
@Author  ：lvy
@Date    ：2021/5/30 21:09
"""
import requests
from bs4 import BeautifulSoup


def get_list(soup_list):
    """
    清洗解析后的网页信息，并以列表形式返回
    :param soup_list: bs_list
    :return:
    """
    ele_list = []
    for ele in soup_list:
        ele_list.append(ele.string)
    return ele_list


# 访问网页、获取信息
headers = {'user-agent': 'my-app/0.0.1'}
url_douban_movie = "https://movie.douban.com/subject/1292064/"
response = requests.get(url=url_douban_movie, headers=headers)
# print(response.text)

# 解析网页
soup = BeautifulSoup(response.text, 'html.parser')
# 美化网页
# print(soup.prettify())

# 获取目标信息
# class_ _代表class为html中的标签，不是python中的标签
# 电影名称
movie_name = soup.find('span', property='v:itemreviewed').text
# 获取简介
synopsis = soup.find(property="v:summary").text
# 导演
director = soup.find(rel="v:directedBy").text
# 编剧
screenwriter = soup.find_all('span', class_="attrs")[1].text
# 演员列表
# # for 遍历数据项， .string获取目标信息
# # print( soup.find_all(rel="v:starring")[0].text)
# actor_list = []
# for ele in soup.find_all(rel="v:starring"):
#     actor_list.append(ele.string)
actor_list = get_list(soup.find_all(rel="v:starring"))
print(actor_list)
# 类型信息
# # print(soup.find_all('span', property="v:genre"))
# type_list = []
# for typ in soup.find_all('span', property="v:genre"):
#     type_list.append(typ.string)
# print(type_list)
type_list = get_list(soup.find_all('span', property="v:genre"))
print(type_list)
# 评分部分
# print(soup.find_all('strong', property="v:average").text)
