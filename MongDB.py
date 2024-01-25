import pymysql

class MyDataBase:

    def __init__(self):

        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.pwd = '123456'
        self.database = 'stock'
        self.connect = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.database)
        self.cursor = self.connect.cursor()

        # 数据库表
        # 基础信息
        self.BASE_STOCK_DETAIL = 'base_stock_detail'
        self.BASE_STOCK_LIST = 'base_stock_list'
        # ROE
        self.BASE_STOCK_ROE = 'base_stock_roe'
        # 流通市值
        self.BASE_STOCK_LTSZ = 'base_stock_ltsz'
        # 市净率
        self.BASE_STOCK_SJL = 'base_stock_sjl'
        self.STOCK_TRADE_DETAIL = ''

    def __enter__(self):
        # 返回游标进行执行操作
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 结束提交数据并关闭数据库
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
