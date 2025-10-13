# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

__version__ = '3.1.2025'

from .constants.holiday import Holiday, holidays, workdays
from .holiday import get_dates
from .holiday import is_workday, is_holiday
from .holiday import get_holidays, get_workdays, find_workday
from .holiday import get_next_nth_workday, get_recent_workday, get_work_dates
from .holiday import get_holiday_detail, get_holiday_info_source
from .solar_terms import SolarTerms, get_solar_terms
from .xingzuo import XINGZUO, get_xingzuo
from .festival import FESTIVAL, FESTIVAL_LUNAR
from .lunar import sol2lun, lun2sol, sol2gz, hour2dz
from .lunar import get_tgdz_year, get_tgdz_date, get_tgdz_hour
from .bazi import get_bazi, get_bazi_lunar
from .bazi import get_wuxing, get_wuxing_lunar
from .bazi import get_marry_match, get_marry_match_lunar
from .bazi import get_chengming, get_chengming_lunar
from .bazi import get_age_by_shuxiang
from .trade_dates import is_tradeday, get_recent_tradeday
from .trade_dates import get_next_nth_tradeday, get_trade_dates


# TODO
# 交易日历支持自定义数据
# 判断农历月大月小，判断是否闰月等
# 增加八字排盘算命等
