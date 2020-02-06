#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   parser.py
# @Time       :   2020/2/3 15:14
# @Version    :   0.1
# @Function  :   解析函数

import re
from bs4 import BeautifulSoup


def getProblemset(contents):
    '''

    :param contents: 需要解析的问题页面内容
    :return:list，[id,问题名称，已提交次数，通过次数，总提交次数]
    '''
    pattern = re.compile('p\((.*?)\);')
    problems = pattern.findall(contents.decode('gb2312'))[1:]
    data = []
    for i in problems:
        i = i.replace("\\", '')
        temp = i.split(',')
        if len(temp) != 6:
            for j in range(len(temp) - 6):
                temp[3] += ' ' + temp.pop(4)
        temp.pop(0)
        data.append(temp)
    return data


def getProblem(contents):
    '''

    :param contents: 需要解析的详细问题页面内容，采用bs4解析
    :return:list，[问题描述，问题输入，问题输出，样例输入，样例输出]
    '''
    contents = BeautifulSoup(contents, 'lxml')
    content = contents.findAll(class_='panel_content')
    return [content[0].text, content[1].text, content[2].text, content[3].text, content[4].text]


def getStatus(contents):
    '''

    :param contents: 状态页面返回的内容
    :return:状态list
    '''
    contents = BeautifulSoup(contents, 'lxml')
    contents = contents.findAll(class_='table_text')[0]
    status = contents.findAll('td')
    data=[]
    temp=[]
    for i in range(len(status)):
        if i % 9 ==0:
            data.append(temp)
            temp=[]
        temp.append(status[i].text)
    data.pop(0)
    return data

