# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""

import requests
import json
import re
from bs4 import BeautifulSoup


def get_data(company, cno):
    assert company in ['顺丰', '中通', '申通', '韵达', '圆通']
    if company == '顺丰':
        flag_str = '%CB%B3%B7%E1IBS'
    if company == '中通':
        flag_str = '%D6%D0%CD%A8'
    if company == '圆通':
        flag_str = 'Բͨ'
    if company == '申通':
        flag_str = '%C9%EA%CD%A8'
    if company == '韵达':
        flag_str = '%D4%CF%B4%EF'
    try:
        url = 'http://www.expba.com/cgi-bin/GInfo.dll?MfcISAPICommand=EmmisTrackGen&w=expba&cemskind=' + str(
            flag_str) + '&cno=' + str(cno)
        r = requests.get(url)
        html = BeautifulSoup(r.text, 'lxml')
        table = html.select('.trackContentTable')[0]
        lines = table.contents[2].string
        lines = re.findall('document.writeln\(MadeLine\("(.*?)",".*?","(.*?)",.*?\)\);', lines)
    except:
        lines = [['NaN', '没有跟踪信息']]
    return lines


if __name__ == '__main__':
    print(get_data('顺丰', 'SF1034236103599'))
    print(get_data('中通', '75409510404179'))
    print(get_data('圆通', 'YT5014934778259'))
