# * coding: utf8 *

import datetime
import pandas as pd

try:
    from .utils import trans_date
    from .constants.hko_calendar import sol_lun, lun_sol, sol_gz
except:
    from chncal.utils import trans_date
    from chncal.constants.hko_calendar import sol_lun, lun_sol, sol_gz
    

# 干支纪年https://baike.baidu.com/item/干支纪年/3383226
# 天干
TG = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
# 地支
DZ = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
DZ_HOUR = {
    '子': (23, 1), '丑': (1, 3), '寅': (3, 5), '卯': (5, 7),
    '辰': (7, 9), '巳': (9, 11), '午': (11, 13), '未': (13, 15),
    '申': (15, 17), '酉': (17, 19), '戌': (19, 21), '亥': (21, 23)
}
# 生肖
SX = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
def _sol_tgdz():
    k1, k2 = 0, 0
    TGDZ = [TG[k1]+DZ[k2]+'('+SX[k2]+')']
    while not (k1 == len(TG)-1 and  k2 == len(DZ)-1):
        if k1 < len(TG)-1:
            k1 += 1
        else:
            k1 = 0
        if k2 < len(DZ)-1:
            k2 += 1
        else:
            k2 = 0
        TGDZ.append(TG[k1]+DZ[k2]+'('+SX[k2]+')')
    return TGDZ
TGDZ = _sol_tgdz()
TGDZ = ['甲子(鼠)', '乙丑(牛)', '丙寅(虎)', '丁卯(兔)', '戊辰(龙)', '己巳(蛇)',
        '庚午(马)', '辛未(羊)', '壬申(猴)', '癸酉(鸡)', '甲戌(狗)', '乙亥(猪)',
        '丙子(鼠)', '丁丑(牛)', '戊寅(虎)', '己卯(兔)', '庚辰(龙)', '辛巳(蛇)',
        '壬午(马)', '癸未(羊)', '甲申(猴)', '乙酉(鸡)', '丙戌(狗)', '丁亥(猪)',
        '戊子(鼠)', '己丑(牛)', '庚寅(虎)', '辛卯(兔)', '壬辰(龙)', '癸巳(蛇)',
        '甲午(马)', '乙未(羊)', '丙申(猴)', '丁酉(鸡)', '戊戌(狗)', '己亥(猪)',
        '庚子(鼠)', '辛丑(牛)', '壬寅(虎)', '癸卯(兔)', '甲辰(龙)', '乙巳(蛇)',
        '丙午(马)', '丁未(羊)', '戊申(猴)', '己酉(鸡)', '庚戌(狗)', '辛亥(猪)',
        '壬子(鼠)', '癸丑(牛)', '甲寅(虎)', '乙卯(兔)', '丙辰(龙)', '丁巳(蛇)',
        '戊午(马)', '己未(羊)', '庚申(猴)', '辛酉(鸡)', '壬戌(狗)', '癸亥(猪)']
# 农历2022年六月十二（公历2022.07.10）是甲子日
TGDZ_BASE_DATE = datetime.date(2022, 7, 10)
# 公历2022.08.24凌晨是甲子时
# TGDZ_BASE_TIME = datetime.datetime(2022, 8, 23, 23, 17, 5)
TGDZ_BASE_TIME = datetime.datetime(2022, 8, 23, 0, 0)


def hour2dz(hour: int = None):
    """获取小时的地支，hour为0-23之间的整数"""
    if hour is None:
        hour = datetime.datetime.now().hour
    hour = int(hour)
    assert 0 <= hour <= 23
    dz = None
    for name, (start, end) in DZ_HOUR.items():
        if hour >= start and hour < end:
            dz = name
    if dz is None:
        dz = '子'
    return dz
    
    
def sol2lun(date=None):
    """公历日期转农历日期"""
    return sol_lun[trans_date(date).strftime('%Y.%m.%d')]


def sol2gz(date=None):
    """公历日期转干支纪日法"""
    return sol_gz[trans_date(date).strftime('%Y.%m.%d')]


def lun2sol(date, run=False):
    """
    农历日期转普通日期，date格式必须形如'2023.02.30'，run为True表示闰月日期
    
    Examples
    --------
    >>> lun2sol('2023.02.30')
    """
    assert isinstance(date, str) and len(date) == 10 and '.' in date
    if run:
        date = date + '闰'
    if date in lun_sol:
        return lun_sol[date]
    else:
        raise ValueError('未找到对应农历日期，请检查输入！')
        
        
def get_tgdz_year(year : int=None):
    """计算年份天干地支"""
    if pd.isnull(year):
        year = datetime.datetime.now().year
    # 农历1984年是甲子年
    year = int(year)
    if year >= 1984:
        return TGDZ[(year-1984) % 60]
    else:
        return TGDZ[-((1984-year) % 60)]
    

def get_tgdz_date(date=None):
    """根据公历日期计算农历干支纪日"""
    date = trans_date(date)
    days = (date - TGDZ_BASE_DATE).days
    if days >= 0:
        return TGDZ[days % 60]
    else:
        return TGDZ[-(abs(days) % 60)]
    
    
def get_tgdz_hour(time=None):
    """
    根据公历时间（小时）计算农历干支纪时
    跟寿星天文历有误差（http://www.nongli.net/sxwnl/）
    """
    if pd.isnull(time):
        time = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    time = str(time)
    dif = pd.to_datetime(time) - TGDZ_BASE_TIME
    days = dif.days
    seconds = dif.seconds + days*24*3600
    hours2 = seconds / 7200
    if hours2 >= 0:
        return TGDZ[int(hours2 % 60)]
    else:
        return TGDZ[-(int(abs(hours2) % 60))-1]
