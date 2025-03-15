# -*- coding: utf-8 -*-

from enum import Enum
import datetime
try:
    from .utils import trans_date
except:
    from chncal.utils import trans_date


class SolarTerms(Enum):
    """中国24节气"""

    the_beginning_of_spring = 'the Beginning of Spring', '立春'
    rain_water = 'Rain Water', '雨水'
    the_waking_of_insects = 'the Waking of Insects', '惊蛰'
    the_spring_equinox = 'the Spring Equinox', '春分'
    pure_brightness = 'Pure Brightness', '清明'
    grain_rain = 'Grain Rain', '谷雨'
    the_beginning_of_summer = 'the Beginning of Summer', '立夏'
    lesser_fullness_of_grain = 'Lesser Fullness of Grain', '小满'
    grain_in_beard = 'Grain in Beard', '芒种'
    the_summer_solstice = 'the Summer Solstice', '夏至'
    lesser_heat = 'Lesser Heat', '小暑'
    greater_heat = 'Greater Heat', '大暑'
    the_beginning_of_autumn = 'the Beginning of Autumn', '立秋'
    the_end_of_heat = 'the End of Heat', '处暑'
    white_dew = 'White Dew', '白露'
    the_autumn_equinox = 'the Autumn Equinox', '秋分'
    code_dew = 'Cold Dew', '寒露'
    frost_descent = "Frost's Descent", '霜降'
    the_beginning_of_winter = 'the Beginning of Winter', '立冬'
    lesser_snow = 'Lesser Snow', '小雪'
    greater_snow = 'Greater Snow', '大雪'
    the_winter_solstice = 'the Winter Solstice', '冬至'
    lesser_cold = 'Lesser Cold', '小寒'
    greater_cold = 'Greater Cold', '大寒'


# 月份和节气对应关系
SOLAR_TERMS_MONTH = {
    1: [SolarTerms.lesser_cold, SolarTerms.greater_cold],
    2: [SolarTerms.the_beginning_of_spring, SolarTerms.rain_water],
    3: [SolarTerms.the_waking_of_insects, SolarTerms.the_spring_equinox],
    4: [SolarTerms.pure_brightness, SolarTerms.grain_rain],
    5: [SolarTerms.the_beginning_of_summer, SolarTerms.lesser_fullness_of_grain],
    6: [SolarTerms.grain_in_beard, SolarTerms.the_summer_solstice],
    7: [SolarTerms.lesser_heat, SolarTerms.greater_heat],
    8: [SolarTerms.the_beginning_of_autumn, SolarTerms.the_end_of_heat],
    9: [SolarTerms.white_dew, SolarTerms.the_autumn_equinox],
    10: [SolarTerms.code_dew, SolarTerms.frost_descent],
    11: [SolarTerms.the_beginning_of_winter, SolarTerms.lesser_snow],
    12: [SolarTerms.greater_snow, SolarTerms.the_winter_solstice],
}


# 参考：https://www.jianshu.com/p/1f814c6bb475，有纠错
# 计算节气用的C值
# 2000年的小寒、大寒、立春、雨水按照20世纪的C值来算
SOLAR_TERMS_C_NUMS = {
    # 节气: [20世纪值， 21世纪值]
    SolarTerms.the_beginning_of_spring: [4.6295, 3.87],
    SolarTerms.rain_water: [19.4599, 18.73],
    SolarTerms.the_waking_of_insects: [6.3926, 5.63],
    SolarTerms.the_spring_equinox: [21.4155, 20.646],
    SolarTerms.pure_brightness: [5.59, 4.81],
    SolarTerms.grain_rain: [20.888, 20.1],
    SolarTerms.the_beginning_of_summer: [6.318, 5.52],
    SolarTerms.lesser_fullness_of_grain: [21.86, 21.04],
    SolarTerms.grain_in_beard: [6.5, 5.678],
    SolarTerms.the_summer_solstice: [22.2, 21.37],
    SolarTerms.lesser_heat: [7.928, 7.108],
    SolarTerms.greater_heat: [23.65, 22.83],
    SolarTerms.the_beginning_of_autumn: [8.35, 7.5],
    SolarTerms.the_end_of_heat: [23.95, 23.13],
    SolarTerms.white_dew: [8.44, 7.646],
    SolarTerms.the_autumn_equinox: [23.822, 23.042],
    SolarTerms.code_dew: [9.098, 8.318],
    SolarTerms.frost_descent: [24.218, 23.438],
    SolarTerms.the_beginning_of_winter: [8.218, 7.438],
    SolarTerms.lesser_snow: [23.08, 22.36],
    SolarTerms.greater_snow: [7.9, 7.18],
    SolarTerms.the_winter_solstice: [22.6, 21.94],
    SolarTerms.lesser_cold: [6.11, 5.4055],
    SolarTerms.greater_cold: [20.84, 20.12],
}

# 有些节气使用公式计算计算的不够准确，需要进行偏移
SOLAR_TERMS_DELTA = {
    (1902, SolarTerms.grain_in_beard): 1,
    (1911, SolarTerms.the_beginning_of_summer): 1,
    (1914, SolarTerms.the_beginning_of_spring): -1,
    (1914, SolarTerms.the_winter_solstice): 1,
    (1915, SolarTerms.the_waking_of_insects): -1,
    (1922, SolarTerms.greater_heat): 1,
    (1923, SolarTerms.rain_water): -1,
    (1925, SolarTerms.lesser_heat): 1,
    (1927, SolarTerms.white_dew): 1,
    (1928, SolarTerms.the_summer_solstice): 1,
    (1942, SolarTerms.the_autumn_equinox): 1,
    (1947, SolarTerms.the_beginning_of_spring): -1,
    (1947, SolarTerms.the_winter_solstice): 1,
    (1948, SolarTerms.the_waking_of_insects): -1,
    (1951, SolarTerms.the_winter_solstice): 1,
    (1978, SolarTerms.lesser_snow): 1,
    (1980, SolarTerms.the_winter_solstice): 1,
    (1982, SolarTerms.lesser_cold): 1,
    (1984, SolarTerms.the_winter_solstice): 1,
    (2000, SolarTerms.greater_cold): 1,
    (2002, SolarTerms.the_beginning_of_autumn): 1,
    (2008, SolarTerms.lesser_fullness_of_grain): 1,
    (2016, SolarTerms.lesser_heat): 1,
    (2019, SolarTerms.lesser_cold): -1,
    (2021, SolarTerms.the_winter_solstice): -1,
    (2026, SolarTerms.rain_water): -1,
    (2082, SolarTerms.greater_cold): 1,
    (2089, SolarTerms.frost_descent): 1,
    (2089, SolarTerms.the_beginning_of_winter): 1,
}


def get_solar_terms(start=None, end=None):
    """
    生成start和end日期之间的24节气，start或end不传，则取当前日期
    
    通用寿星公式：https://www.jianshu.com/p/1f814c6bb475，有纠错
    通式寿星公式：[Y×D+C]-L
    []里面取整数；Y=年数的后2位数；D=0.2422；L=Y/4，小寒、大寒、立春、雨水的 L=(Y-1)/4
    """
    start_bk = start
    start = trans_date(start)
    end = trans_date(end)
    if not 1900 <= start.year <= 2100 or not 1900 <= end.year <= 2100:
        raise NotImplementedError('only year between [1900, 2100] supported')
    D = 0.2422
    result = []
    year, month = start.year, start.month
    while year < end.year or (year == end.year and month <= end.month):
        # 按月计算节气
        for solar_term in SOLAR_TERMS_MONTH[month]:
            nums = SOLAR_TERMS_C_NUMS[solar_term]
            C = nums[0] if year < 2000 else nums[1]
            # 2000 年的小寒、大寒、立春、雨水按照 20 世纪的 C 值来算
            if year == 2000 and solar_term in [
                SolarTerms.lesser_cold,
                SolarTerms.greater_cold,
                SolarTerms.the_beginning_of_spring,
                SolarTerms.rain_water,
            ]:
                C = nums[0]
            Y = year % 100
            L = int(Y / 4)
            if solar_term in [
                SolarTerms.lesser_cold,
                SolarTerms.greater_cold,
                SolarTerms.the_beginning_of_spring,
                SolarTerms.rain_water,
            ]:
                L = int((Y - 1) / 4)
            day = int(Y * D + C) - L
            # 计算偏移量
            delta = SOLAR_TERMS_DELTA.get((year, solar_term))
            if delta:
                day += delta
            _date = datetime.date(year, month, day)
            if _date < start or _date > end:
                continue
            result.append((_date, solar_term.value[1]))
        if month == 12:
            year, month = year + 1, 1
        else:
            month += 1
    if start_bk is not None:
        from dramkit.dttools import copy_format
        result = [(copy_format(x[0], start_bk), x[1]) for x in result]
    return result
