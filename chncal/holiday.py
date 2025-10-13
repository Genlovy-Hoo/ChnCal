# -*- coding: utf-8 -*-

import datetime
try:
    from .utils import trans_date, copy_format_from_start
    from .utils import get_file_path, load_yml
    from .constants.holiday import holidays, workdays
except:
    from chncal.utils import trans_date, copy_format_from_start
    from chncal.utils import get_file_path, load_yml
    from chncal.constants.holiday import holidays, workdays
    
    
def _validate_date(*dates):
    """check if the date(s) is supported"""
    if len(dates) != 1:
        return list(map(_validate_date, dates))
    date = trans_date(dates[0])
    if not isinstance(date, datetime.date):
        raise NotImplementedError('unsupported type {}, expected type is datetime.date'.format(type(date)))
    min_year, max_year = min(holidays.keys()).year, max(holidays.keys()).year
    if not (min_year <= date.year <= max_year):
        raise NotImplementedError(
            'no available data for year {}, only year between [{}, {}] supported'.format(date.year, min_year, max_year)
        )
    return date


@copy_format_from_start
def get_dates(start=None, end=None, copy_format=True):
    """
    get dates between start date and end date. (includes start date and end date)
    """
    start, end = map(trans_date, (start, end))
    delta_days = (end - start).days
    return [start + datetime.timedelta(days=delta) for delta in range(delta_days+1)]


def is_workday(date=None):
    """
    check if one date is workday in China.
    in other words, Chinese people works at that day.
    """
    date = _validate_date(date)
    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))


def is_holiday(date=None):
    """
    check if one date is holiday in China.
    in other words, Chinese people get rest at that day.
    """
    return not is_workday(date)


@copy_format_from_start
def get_holidays(start=None, end=None, include_weekends=True, **kwargs):
    """
    get holidays between start date and end date. (includes start date and end date)
    """
    start, end = _validate_date(start, end)
    if include_weekends:
        return list(filter(is_holiday, get_dates(start, end, copy_format=False)))
    return list(filter(lambda x: x in holidays, get_dates(start, end, copy_format=False)))


@copy_format_from_start
def get_workdays(start=None, end=None, **kwargs):
    """
    get workdays between start date and end date. (includes start date and end date)
    """
    start, end = _validate_date(start, end)
    dates = get_dates(start, end, copy_format=False)
    return list(filter(is_workday, dates))


def get_work_dates(start_date=None, end_date=None, **kwargs):
    return get_workdays(start_date, end_date, **kwargs)


@copy_format_from_start
def _find_workday(date=None, delta_days=0, **kwargs):
    date = trans_date(date or datetime.date.today())
    if delta_days >= 0 and is_workday(date):
        delta_days += 1
    sign = 1 if delta_days >= 0 else -1
    for i in range(abs(delta_days)):
        if delta_days < 0 or i:
            date += datetime.timedelta(days=sign)
        while not is_workday(date):
            date += datetime.timedelta(days=sign)
    return date


def find_workday(delta_days=0, date=None):
    """
    find the workday after {delta_days} days. 查找date之后的第delta_days个工作日
    """
    return _find_workday(date=date, delta_days=delta_days)


@copy_format_from_start
def get_next_nth_workday(date=None, n=1, **kwargs):
    """
    给定日期date，返回其后第n个工作日日期，n可为负数（返回结果在date之前）
    若n为0，直接返回date
    """
    date = trans_date(date)
    n_add = -1 if n < 0 else 1
    n = abs(n)
    tmp = 0
    while tmp < n:
        date = date + datetime.timedelta(n_add)
        if is_workday(date):
            tmp += 1
    return date


@copy_format_from_start
def get_recent_workday(date=None, dirt='post', **kwargs):
    """
    若date为工作日，则直接返回，否则返回下一个(dirt为post时)或上一个(dirt为pre时)工作日
    """
    date = trans_date(date)
    tdelta = datetime.timedelta(1)
    if dirt == 'post':
        while not is_workday(date):
            date =  date + tdelta
    elif dirt == 'pre':
        while not is_workday(date):
            date =  date - tdelta
    return date


def get_holiday_detail(date=None):
    """
    check if one date is holiday in China,
    and return the holiday name (None if it's a normal day)
    """
    date = _validate_date(date)
    if date in workdays.keys():
        return False, workdays[date]
    elif date in holidays.keys():
        return True, holidays[date]
    else:
        return date.weekday() > 4, None
    
    
def get_holiday_info_source(year):
    data = load_yml(get_file_path('holiday.yml', 'data'))
    return data[int(year)]['info_from']
