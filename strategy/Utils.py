# #2-1 过滤停牌股票
# def filter_paused_stock(stock_list):
# 	current_data = get_current_data()
# 	return [stock for stock in stock_list if not current_data[stock].paused]

# 过滤入口
def filter_entrance(stock_list):
    result = []
    for stock in stock_list:
        if filter_st_stock(stock) and filter_kcbj_stock(stock):
            result.append(stock)
    return result


# 2-2 过滤ST及其他具有退市标签的股票
def filter_st_stock(stock):
    return True if 'ST' not in stock['mc'] and '*' not in stock['mc'] and '退' not in stock['mc'] else False


# 2-5 过滤科创北交股票
def filter_kcbj_stock(stock):
    return True if stock['dm'][:2] != '68' and stock['dm'][:2] != '30' else False

# #2-3 过滤涨停的股票
# def filter_limitup_stock(context, stock_list):
# 	last_prices = history(1, unit='1m', field='close', security_list=stock_list)
# 	current_data = get_current_data()
# 	return [stock for stock in stock_list if stock in context.portfolio.positions.keys()
# 			or last_prices[stock][-1] < current_data[stock].high_limit]
#
# #2-4 过滤跌停的股票
# def filter_limitdown_stock(context, stock_list):
# 	last_prices = history(1, unit='1m', field='close', security_list=stock_list)
# 	current_data = get_current_data()
# 	return [stock for stock in stock_list if stock in context.portfolio.positions.keys()
# 			or last_prices[stock][-1] > current_data[stock].low_limit]
