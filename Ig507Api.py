import requests

license = '9F83CEA9-6399-A249-E1BC-94B317827892'


def get_stock_list() -> list:
    """ 基础股票列表 """
    stock_list = []
    try:
        url = f'http://ig507.com/data/base/gplist?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_list = resp.json()
    except Exception as e:
        print(f'股票基础列表错误:{e}')
    finally:
        return stock_list


def get_stock_trade_detail(stock_code, time_level='Day') -> dict:
    """ 获取股票历史分时交易信息 """
    stock = []
    try:
        url = f'https://ig507.com/data/time/history/trade/{stock_code}/{time_level}?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock = resp.json()
    except Exception as e:
        print(f'获取股票历史分时交易信息错误:{e}')
    finally:
        return stock


def get_stock_roe() -> list:
    """ 获取股票roe """
    stock_roe = []
    try:
        url = f'https://ig507.com/data/all/roe?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_roe = resp.json()
    except Exception as e:
        print(f'获取股票roe错误:{e}')
    finally:
        return stock_roe


def get_stock_ltsz() -> list:
    """ 获取股票流通市值 """
    stock_ltsz = []
    try:
        url = f'https://ig507.com/data/all/ltsz?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_ltsz = resp.json()
    except Exception as e:
        print(f'获取股票流通市值错误:{e}')
    finally:
        return stock_ltsz


def get_stock_sjl() -> list:
    """ 获取市净率 """
    stock_sjl = []
    try:
        url = f'https://ig507.com/data/all/sjl?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_sjl = resp.json()
    except Exception as e:
        print(f'获取市净率错误:{e}')
    finally:
        return stock_sjl


def get_stock_detail(dm) -> dict:
    """ 获取基本面信息 """
    stock_detail = []
    try:
        url = f'https://ig507.com/data/time/f10/info/{dm}?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_detail = resp.json()
    except Exception as e:
        print(f'获取基本面信息错误:{e}')
    finally:
        return stock_detail

def get_stock_zt() -> list:
    date = '2024-01-25'
    stock_detail = []
    try:
        url = f'https://ig507.com/data/time/zdtgc/ztgc/{date}?licence={license}'
        resp = requests.get(url)
        if resp.status_code == 200:
            stock_detail = resp.json()
            # 过滤科创
            stock_detail = list(filter(lambda s: s['dm'][2:3] != '8' and s['dm'][2:3] != '3', stock_detail))
            # 过滤过大或者过小的总市值
            # stock_detail = list(filter(lambda s: s['zsz'] > 20000000000 or s['zsz'] < 1000000, stock_detail))
            # 过滤过高的换手率
            # stock_detail = list(filter(lambda s: s['hs'] > 20000000000 or s['zsz'] < 1000000, stock_detail))
    except Exception as e:
        print(f'获取基本面信息错误:{e}')
    finally:
        return stock_detail

if __name__ == '__main__':
    stocks = get_stock_zt()
    stocks.sort(key=lambda s: s['dm'])
    for i in stocks:
        print(i['dm'] + '-' + i['mc'] + '-' + i['tj'])