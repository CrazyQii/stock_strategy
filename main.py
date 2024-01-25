import Ig507Api
import MongDB
import talib

mongo = MongDB.MyDataBase()

if __name__ == '__main__':

    base_stock_list = Ig507Api.get_stock_list()
    print("获取完成")
    collections = mongo.get_mongo_col(mongo.BASE_STOCK_LIST)

    for stock in base_stock_list:
        try:
            collections.insert_one(stock)
        except Exception as e:
            continue


    # time.sleep(2)
    # # 股票市净率
    # base_stock_roe = get_stock_roe()
    # time.sleep(2)
    # # 股票流通市值
    # base_stock_ltsz = get_stock_ltsz()
    # # 汇总数据
    # stock_list = []
    #
    #
    # for stock, roe, ltsz in itertools.product(base_stock_list, base_stock_roe, base_stock_ltsz):
    #     if stock['dm'] == roe['dm'] and stock['jys']+stock['dm'] == ltsz['dm']:
    #         stock.update(roe)
    #         stock.update(ltsz)
    #         stock_list.append(stock)
    #         print(stock)

    # print(num)
    # stock_list.sort(key=lambda stock: stock['code'])
    # stock_list.sort(key=lambda stock: stock['code'], reverse=True)
    # print(stock_list)
