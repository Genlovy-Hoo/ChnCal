# -*- coding: utf-8 -*-

import os
import time
import datetime
import yaml
from functools import wraps
import pandas as pd


def get_file_path(fname, dirname='constants'):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(cur_dir, dirname, fname)    


def _load_yml(fpath, **kwargs_open):
    with open(fpath, **kwargs_open) as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data


def load_yml(*args, **kwargs):
    if 'encoding' not in kwargs:
        for en in ['utf-8', None, 'gbk']:
            try:
                kwargs.update({'encoding': en})
                return _load_yml(*args, **kwargs)
            except:
                pass
    return _load_yml(*args, **kwargs)


def trans_date(date):
    if pd.isnull(date):
        date = datetime.datetime.now()
    if isinstance(date, str):
        date = pd.to_datetime(date)
    elif isinstance(date, int):
        date = pd.to_datetime(str(date))
    elif isinstance(date, time.struct_time):
        date = pd.to_datetime(
               datetime.datetime.fromtimestamp(time.mktime(date)))
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date


def copy_format_from_start(func):
    """
    作为装饰器从start(第一个参数)复制日期时间格式
    """
    @wraps(func)
    def copyer(*args, **kwargs):
        start = None if len(args) == 0 else args[0]
        res = func(*args, **kwargs)
        if start is not None and kwargs.get('copy_format', True):
            from dramkit.dttools import copy_format
            res = copy_format(res, start)
        return res
    return copyer
