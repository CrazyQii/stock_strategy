import pymongo
from MongDB import MyDataBase
from strategy.Utils import *

db = MyDataBase()

def get_dragon_stock():
    stocks = []
    with db as f:
        # sql = f'select roe.dm, roe.mc, roe.roe, ltsz.zsz from base_stock_roe as roe, base_stock_ltsz as ltsz where roe.mc = ltsz.mc order by zsz, roe.roe'
        sql = f'select roe.dm, roe.mc, roe.roe, ltsz.zsz from base_stock_roe as roe, base_stock_ltsz as ltsz where roe.mc = ltsz.mc and roe > 0.3 order by ltsz'
        f.execute(sql)
        for stock in f.fetchall():
            if filter_st_stock(stock) and filter_dragon_stock(stock) and filter_kcbj_stock(stock):
                stocks.append(stock)
                print(stock)
    return stocks

def filter_st_stock(stock):
    return True if 'ST' not in stock[1] and '*' not in stock[1] else False

def filter_dragon_stock(stock):
    return True if '龙' in stock[1] else False

def filter_kcbj_stock(stock):
    return False if stock[0][:2] == '68' or stock[0][:2] == '30' else True

def filter_new_stock(stock_list, d):
    return [stock for stock in stock_list if not yesterday - get_security_info(stock).start_date < datetime.timedelta(days=d)]

if __name__ == '__main__':
    get_dragon_stock()