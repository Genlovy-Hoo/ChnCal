# * coding: utf8 *

import datetime
import pandas as pd
try:
    from .lunar import sol2gz, get_tgdz_hour, lun2sol, sol2lun, hour2dz, SX
    from .wuxing import TGWX, DZWX, TGDZNYWX
    from .marry_match import MARRY_MATCH
    from .constants.chengming import w_year, w_month, w_date, w_hour, song
except:
    from chncal.lunar import sol2gz, get_tgdz_hour, lun2sol, sol2lun, hour2dz, SX
    from chncal.wuxing import TGWX, DZWX, TGDZNYWX
    from chncal.marry_match import MARRY_MATCH
    from chncal.constants.chengming import w_year, w_month, w_date, w_hour, song
    
    
def get_bazi(time=None):
    """
    根据公历时间生成八字
    
    Examples
    --------
    >>> get_bazi('1992.05.14 18:00')
    """
    return sol2gz(time) + ',' + get_tgdz_hour(time) + '时'


def get_bazi_lunar(time, run=False):
    """
    根据农历时间生成八字，time格式必须形如'2023.02.30 19:30:20'，时分秒可以不写，
    run为True表示闰月日期
    
    Examples
    --------
    >>> get_bazi_lunar('2023.02.30')
    """
    assert isinstance(time, str) and '.' in time
    date = lun2sol(time[:10], run=run)
    time = date + time[10:]
    return get_bazi(time)


def get_wuxing(time=None):
    """根据公历时间获取五行信息"""
    bazi = get_bazi(time)
    wx_detail = {x: TGDZNYWX[x[:2]]+'(%s, %s)'%(TGWX[x[0]], DZWX[x[1]]) for x in bazi.split(',')}
    wx = [v[2] for k, v in wx_detail.items()]
    return wx, wx_detail


def get_wuxing_lunar(time, run=False):
    """根据农历时间获取五行信息，time格式必须形如'2023.02.30 19:30:20'，run为True表示闰月日期"""
    bazi = get_bazi_lunar(time, run=run)
    wx_detail = {x: TGDZNYWX[x[:2]]+'(%s, %s)'%(TGWX[x[0]], DZWX[x[1]]) for x in bazi.split(',')}
    wx = [v[2] for k, v in wx_detail.items()]
    return wx, wx_detail


def get_marry_match(time=None):
    """根据公历时间获取属相合婚信息"""
    sx = sol2gz(time)[3]
    return {sx: MARRY_MATCH[sol2gz(time)[3]]}


def get_marry_match_lunar(time, run=False):
    """根据农历时间获取属相合婚信息，time格式必须形如'2023.02.30 19:30:20'，run为True表示闰月日期"""
    assert isinstance(time, str) and '.' in time
    date = lun2sol(time[:10], run=run)
    sx = sol2gz(date)[3]
    return {sx: MARRY_MATCH[sol2gz(time)[3]]}


def _time2dz(time=None):
    if pd.isnull(time):
        hour = datetime.datetime.now().hour
    else:
        hour = pd.to_datetime(str(time)).hour
    return hour2dz(hour)


def get_chengming(time=None):
    """称命，传入公历时间"""
    bazi = get_bazi(time)
    date = sol2lun(time)
    wy = float(w_year[bazi[:5]])
    wm = float(w_month[date[5:7]])
    wd = float(w_date[date[8:]])
    wh = float(w_hour[_time2dz(time)])
    w = float(round(wy+wm+wd+wh, 2))
    sing = song[str(w)]
    result = {
        'weight': w,
        'bazi': bazi,
        'song': sing,
        'weight_split': (wy, wm, wd, wh)
    }
    return result


def get_chengming_lunar(time, run=False):
    """
    称命，传入农历时间
    
    Examples
    --------
    >>> get_chengming_lunar('2023.02.30 09:30:00')
    """
    assert isinstance(time, str) and '.' in time
    bazi = get_bazi_lunar(time, run=run)
    wy = float(w_year[bazi[:5]])
    wm = float(w_month[time[5:7]])
    wd = float(w_date[time[8:10]])
    hour = int(time[11:13]) if len(time) >= 13 else 0
    wh = float(w_hour[hour2dz(hour)])
    w = float(round(wy+wm+wd+wh, 2))
    sing = song[str(w)]
    result = {
        'weight': w,
        'bazi': bazi,
        'song': sing,
        'weight_split': (wy, wm, wd, wh)
    }
    return result


def get_age_by_shuxiang(shuxiang, year: int = None, return_n: int = 10):
    """根据属性获取可能年龄"""
    assert isinstance(shuxiang, str) and shuxiang in SX
    now_year = datetime.datetime.now().year if year is None else int(year)
    base_year, base_sx = 2022, '虎'
    res = {}
    n = 0
    year, idx = base_year, SX.index(base_sx)
    while n < return_n:
        if SX[idx] == shuxiang:
            age = now_year - year
            if age >= 0:
                res[year] = age
                n += 1
        year -= 1
        if idx == 0:
            idx = 11
        else:
            idx -= 1    
    return res
