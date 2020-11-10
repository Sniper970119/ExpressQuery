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

import test_data


def get_data():
    data = test_data.json
    try:
        res = data['result']['showapi_res_body']['data']
    except:
        res = [{'context': 'error', 'time': 'error'}]

    try:
        mailNo = data['result']['showapi_res_body']['mailNo']
    except:
        mailNo = 'error'

    try:
        expTextName = data['result']['showapi_res_body']['expTextName']
    except:
        expTextName = 'error'

    return_res = [res[0], mailNo, expTextName]

    return return_res


if __name__ == '__main__':
    print(get_data())
