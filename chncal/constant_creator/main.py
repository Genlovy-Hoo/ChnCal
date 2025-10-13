# -*- coding: utf-8 -*-

try:
    from .holiday import create_holiday_constant
    from .chengming import create_chengming_constant
    from .hko_calendar import create_hko_constant
    from .trade_dates import create_trade_dates_constant
except:
    from chncal.constant_creator.holiday import create_holiday_constant
    from chncal.constant_creator.chengming import create_chengming_constant
    from chncal.constant_creator.hko_calendar import create_hko_constant
    from chncal.constant_creator.trade_dates import create_trade_dates_constant

if __name__ == '__main__':
    create_holiday_constant()
    create_chengming_constant()
    create_hko_constant()
    create_trade_dates_constant()