import time

import Ig507Api
from MongDB import MyDataBase
import talib


db = MyDataBase()

def update_base_stock_list():
    """ 获取基础信息 """
    base_stock_list = Ig507Api.get_stock_list()
    values = []
    for stock in base_stock_list:
        print(stock)
        update_stock_detail(stock['dm'])
        time.sleep(2)
        values.append(tuple(stock.values()))
    with db as f:
        sql = f"replace into {db.BASE_STOCK_LIST}(`dm`, `mc`, `jys`) values (%s, %s, %s) "
        result = f.executemany(sql, values)
        print('获取基础信息完成,更新数量：' + str(result))


def update_stock_roe():
    """ 获取ROE """
    base_stock_roe = Ig507Api.get_stock_roe()
    values = []
    for stock in base_stock_roe:
        stock_format = {
            'dm': stock['dm'],
            'mc': stock['mc'],
            'jzc': stock['jzc'],
            'jlr': stock['jlr'],
            'syld': stock['syld'],
            'sjl': stock['sjl'],
            'mll': stock['mll'],
            'jll': stock['jll'],
            'roe': stock['roe']
        }
        values.append(tuple(stock_format.values()))
    with db as f:
        try:
            sql = f"insert into {db.BASE_STOCK_ROE}(`dm`, `mc`, `jzc`, `jlr`, `syld`, `sjl`, `mll`, `jll`, `roe`) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s) on duplicate key update " \
                  "`jzc` = values(jzc), `jlr` = values(jlr), `syld` = values(syld), `sjl` = values(sjl), `mll` = values(mll), `jll` = values(jll), `roe` = values(roe)"
            result = f.executemany(sql, values)
            print('获取ROE完成,更新数量：' + str(result))
        except Exception as e:
            print(e)


def update_stock_ltsz():
    """ 获取流通市值 """
    base_stock_ltsz = Ig507Api.get_stock_ltsz()
    values = []
    for stock in base_stock_ltsz:
        stock_format = {
            'dm': stock['dm'][2:],
            'mc': stock['mc'],
            'zsz': stock['zsz'],
            'ltsz': stock['ltsz'],
            't': stock['t'],
            'c': stock['c']
        }
        values.append(tuple(stock_format.values()))
    with db as f:
        try:
            sql = f"insert into {db.BASE_STOCK_LTSZ}(`dm`, `mc`, `zsz`, `ltsz`, `t`, `c`) " \
                  "values (%s, %s, %s, %s, %s, %s) on duplicate key update `zsz`=values(zsz), `ltsz`=values(ltsz), `t`=values(t), `c` = values(c)"
            result = f.executemany(sql, values)
            print('获取流通市值完成,更新数量：' + str(result))
        except Exception as e:
            print(e)


def update_stock_sjl():
    """ 获取市净率 """
    base_stock_sjl = Ig507Api.get_stock_sjl()
    values = []
    for stock in base_stock_sjl:
        print(stock)
        stock_format = {
            'dm': stock['dm'][2:],
        }


def update_stock_trade_detail():
    stock_trade_detail = Ig507Api.get_stock_trade_detail()
    collections = mongo.get_mongo_col(mongo.BASE_STOCK_LTSZ)

def update_stock_detail(dm):
    """ 标的基本面信息 """
    # base_stock_detail = Ig507Api.get_stock_detail(dm)
    with db as f:

        try:
            sql = f"select * from {db.BASE_STOCK_DETAIL} where dm = %s"
            f.execute(sql, tuple(dm))
            stock = f.fetchone()
            print(stock['dm'])


            # stock_detail = {
            #     'dm': dm,
            #     'name': base_stock_detail['name'],
            #     'ename': base_stock_detail['ename'],
            #     'market': base_stock_detail['market'],
            #     'ldate': base_stock_detail['ldate'],
            #     'rdate': base_stock_detail['rdate'],
            #     'rprice': base_stock_detail['rprice'],
            #     'instype': base_stock_detail['instype'],
            #     'organ': base_stock_detail['organ']
            # }
            # values = tuple(stock_detail.values())
            # sql = f"replace into {db.BASE_STOCK_DETAIL}(`dm`, `name`,`ename`,`market`,`ldate`,`rdate`,`rprice`,`instype`,`organ`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # f.execute(sql, values)
            # print('获取标的基本面信息,更新：' + str(stock_detail))
        except Exception as e:
            print(e)


def main():
    update_base_stock_list()
    # update_stock_roe()
    # update_stock_ltsz()
    # update_stock_sjl()
    # update_stock_detail('000001')

if __name__ == '__main__':
    main()


