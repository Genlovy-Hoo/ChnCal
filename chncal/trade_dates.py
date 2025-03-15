# -*- coding: utf-8 -*-

import datetime
import pandas as pd
try:
    from .utils import trans_date, copy_format_from_start
    from .constants.trade_dates import MARKETS, trade_dates
    from .holiday import is_workday
except:
    from chncal.utils import trans_date, copy_format_from_start
    from chncal.holiday import is_workday
    from chncal.constants.trade_dates import MARKETS, trade_dates


def _is_tradeday(date=None):
    return is_workday(date) and date.weekday() not in [5, 6]


def is_tradeday(date=None, market='SSE'):
    """判断是否为交易日"""
    market = market.upper()
    assert market in MARKETS, '未识别的交易所，请检查！'
    date = trans_date(date)    
    if date < MARKETS[market]:
        return False  # 小于首个交易日的直接视为非交易日
    if (market, date) in trade_dates:
        return bool(trade_dates[(market, date)])
    return _is_tradeday(date)


@copy_format_from_start
def get_recent_tradeday(date=None, dirt='post', market='SSE'):
    """
    查询最近的交易日，若date为交易日，则直接返回date，否则返回下一个(dirt='post')或上一个(dirt='pre')交易日
    """
    assert dirt in ['post', 'pre']
    date = trans_date(date)
    tdelta = datetime.timedelta(1)
    if dirt == 'post':
        while not is_tradeday(date, market=market):
            date = date + tdelta
    elif dirt == 'pre':
        while not is_tradeday(date, market=market):
            if date.date() < MARKETS[market]:
                date = MARKETS[market]
                break
            date = date - tdelta
    return date


@copy_format_from_start
def get_next_nth_tradeday(date=None, n=1, market='SSE'):
    """
    | 给定日期date，返回其后第n个交易日日期，n可为负数（返回结果在date之前）
    | 若n为0，直接返回date
    """
    date = trans_date(date)
    n_add = -1 if n < 0 else 1
    n = abs(n)
    tmp = 0
    while tmp < n:
        if n_add == -1 and date.date() <= MARKETS[market]:
            break
        date = date + datetime.timedelta(n_add)
        if is_tradeday(date, market=market):
            tmp += 1
    return date


@copy_format_from_start
def get_trade_dates(start_date, end_date=None, market='SSE'):
    """
    取指定起止日期内的交易日期（周内的工作日）
    """
    start_date = trans_date(start_date)
    end_date = trans_date(end_date)
    dates = pd.date_range(start_date, end_date)
    dates = [x for x in dates if is_tradeday(x, market=market)]
    return dates
