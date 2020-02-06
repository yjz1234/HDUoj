#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   loginHdu.py
# @Time       :   2020/2/3 13:57
# @Version    :   0.1
# @Function  :   d登录的实现


url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'acm.hdu.edu.cn',
    'Origin': 'http://acm.hdu.edu.cn',
    'Referer': 'http://acm.hdu.edu.cn/listproblem.php?vol=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


# 获取用户信息，组装
def getUser(user,passwd):
    '''

    :return: dict,
        login_info = {
            'username': user,
            'userpass': passswd,
            'login': button_string
        }
    '''
    button_string = 'Sign In'

    login_info = {
        'username': user,
        'userpass': passwd,
        'login': button_string
    }

    return login_info


# 登录HDUoj
def loginHdu(session,username,password):
    '''

    :param session: 使用一致的会话，保证cookie相同，从而实现其他功能
    :return: session，requests的会话，具有自动更新cookie的功能
    '''
    login_info = getUser(username,password)
    session.post(url, headers=headers, data=login_info)
    return session
