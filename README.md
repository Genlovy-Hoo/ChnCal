# 中国节假日、农历、八字、A股交易日历查询工具

## 安装

```shell
pip install chncal dramkit --upgrade
```

项目地址: Gitee: [ChnCal](https://gitee.com/glhyy/ChnCal)；Github: [ChnCal](https://github.com/Genlovy-Hoo/ChnCal/)；Pypi: [chncal](https://pypi.org/project/chncal/)。

## 接口说明

参数中的`date`或`time`不传即默认为当前日期时间，`date`传参格式可为datetime格式或常见的文本格式或整数格，（如`20250315`，`2025.03.15`，`2025-03-15`，`datetime.date(2025, 3, 15)`都可以），返回格式默认与输入格式相同。

```python
from chncal import *  # 接口名称
```

### 中国节假日和工作日历查询（从2001年起）

- `is_workday(date=None)`: 判断date是否为工作日
- `is_holiday(date=None)`: 判断date是否为假期
- `get_holidays(start=None, end=None, include_weekends=True)`: 获取start和end之间的节假期列表，include_weekends设置是否包含正常周末
- `get_workdays(start=None, end=None)`: 获取start和end之间的工作日列表
- `find_workday(delta_days=0, date=None)`: 查找date之后的第delta_days个工作日
- `get_next_nth_workday(date=None, n=1)`: 返回date后第n个工作日日期，n可为负数（返回结果在date之前），若n为0，直接返回date
- `get_recent_workday(date=None, dirt='post')`: 若date为工作日，则直接返回，否则返回下一个(dirt为post时)或上一个(dirt为pre时)工作日

### 星座查询

- `get_xingzuo(date=None)`: 查询date的星座

### 农历查询

- `get_solar_terms(start=None, end=None)`: 查询start和end日期之间的24节气列表
- `sol2lun(date=None)`: 公历日期转农历日期
- `sol2gz(date=None)`: 公历日期转干支纪日法
- `lun2sol(date, run=False)`: 农历日期转普通日期，date格式必须形如'2023.02.30'，run为True表示闰月日期

### 八字查询

- `get_bazi(time=None)`: 根据公历时间生成八字
- `get_bazi_lunar(time, run=False)`: 根据农历时间生成八字，time格式必须形如'2023.02.30 19:30:20'，时分秒可以不写，run为True表示闰月日期
- `get_wuxing(time=None)`:  根据公历时间获取五行信息
- `get_wuxing_lunar(time, run=False)`: 根据农历时间获取五行信息，time格式必须形如'2023.02.30 19:30:20'，run为True表示闰月日期
- `get_marry_match(time=None)`: 根据公历时间获取属相合婚信息
- `get_marry_match_lunar(time, run=False)`: 根据农历时间获取属相合婚信息，time格式必须形如'2023.02.30 19:30:20'，run为True表示闰月日期
- `get_chengming(time=None)`: 称命，传入公历时间
- `get_chengming_lunar(time, run=False)`: 称命，传入农历时间
- `get_age_by_shuxiang(shuxiang, year: int = None)`: 根据属性获取可能年龄

### A股交易日历查询

- `is_tradeday(date=None`: 判断是否为交易日
- `get_recent_tradeday(date=None, dirt='post')`: 查询最近的交易日，若date为交易日，则直接返回date，否则返回下一个(dirt='post')或上一个(dirt='pre')交易日
- `get_next_nth_tradeday(date=None, n=1)`: 
- 给定日期date，返回其后第n个交易日日期，n可为负数（返回结果在date之前），若n为0，直接返回date
- `get_trade_dates(start_date, end_date=None)`: 取指定起止日期内的交易日期（周内的工作日）

## 参考

chinese_calendar: [github](https://github.com/LKI/chinese-calendar) 
