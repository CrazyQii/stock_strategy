import requests
import time
import talib

license = '9F83CEA9-6399-A249-E1BC-94B317827892'

stock_list = []

def get_stock_list() -> list:
    """ 基础股票列表 """
    try:
        url = f'http://ig507.com/data/base/gplist?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            for item in resp.json():
                stock_list.append({
                    'code': item['dm'],
                    'name': item['mc'],
                    'jys': item['jys']
                })
    except Exception as e:
        print(f'股票基础列表错误:{e}')
    finally:
        return stock_list

def get_stock_detail(stock_code, time_level) -> dict:
    """ 获取股票历史分时交易信息 """
    stock = {}
    try:
        url = f'https://ig507.com/data/time/history/trade/{stock_code}/{time_level}?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            print(resp.json())
    except Exception as e:
        print(e)
    finally:
        return stock


if __name__ == '__main__':
    # get_stock_list()
    print(get_stock_detail('688039', 'Day'))
    # stock_list.sort(key=lambda stock: stock['code'])
    # stock_list.sort(key=lambda stock: stock['code'], reverse=True)
    print(stock_list)