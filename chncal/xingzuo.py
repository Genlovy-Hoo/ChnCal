# * coding: utf8 *


try:
    from .utils import trans_date
except:
    from chncal.utils import trans_date
    
    
XINGZUO = {
    '摩羯座': {
        'dt_rng': ('1222', '0119'),
        'desc': '摩羯座的人以稳重、务实、有责任感著称。他们注重事业和成就，有很强的自律性，但有时会显得过于严肃或缺乏灵活性。'
        },
    '水瓶座': {
        'dt_rng': ('0120', '0218'),
        'desc': '水瓶座的人以独立、创新、人道主义著称。他们思想开放，善于接受新观念，追求自由和平等。水瓶座的人通常性格开朗，但有时会显得冷漠或过于理性。'
        },
    '双鱼座': {
        'dt_rng': ('0219', '0320'),
        'desc': '双鱼座的人以温柔、敏感、富有同情心著称。他们富有创造力，喜欢沉浸在自己的世界中，但有时会显得过于理想化或容易受他人影响。'
        },
    '白羊座': {
        'dt_rng':  ('0321', '0419'),
        'desc': '白羊座是黄道十二星座的第一个星座，象征着新的开始。白羊座的人通常充满活力、热情、勇敢，喜欢冒险和挑战。他们性格直爽，行动力强，但有时可能会显得冲动和缺乏耐心。'
        },
    '金牛座': {
        'dt_rng': ('0420', '0520'),
        'desc': '金牛座的人以稳重、踏实著称。他们热爱生活，注重物质享受，对美好事物有很高的追求。金牛座的人通常耐心十足，但有时会显得固执，不喜欢改变。'
        },
    '双子座': {
        'dt_rng': ('0521', '0621'),
        'desc': '双子座是风象星座，以聪明、灵活、善于沟通著称。双子座的人好奇心旺盛，喜欢探索新事物，思维敏捷，但有时会显得善变，难以捉摸。'
        },
    '巨蟹座': {
        'dt_rng': ('0622', '0722'),
        'desc': '巨蟹座的人以家庭为中心，情感丰富，富有同情心。他们善良、体贴，对家人和朋友非常忠诚，但有时会显得情绪化，对外界的批评比较敏感。'
        },
    '狮子座': {
        'dt_rng': ('0723', '0822'),
        'desc': '狮子座的人天生具有领导才能，自信、热情、充满魅力。他们喜欢成为众人关注的焦点，有很强的责任感，但有时会显得自负或过于自我中心。'
        },
    '处女座': {
        'dt_rng': ('0823', '0922'),
        'desc': '处女座的人以完美主义著称，注重细节，追求高品质的生活。他们聪明、勤奋、有条理，但有时会显得过于挑剔或过于关注细节而忽略了整体。'
        },
    '天秤座': {
        'dt_rng': ('0923', '1023'),
        'desc': '天秤座的人追求和谐与平衡，善于社交，具有很强的审美能力。他们性格温和，善于调解冲突，但有时会显得优柔寡断，难以做出决策。'
        },
    '天蝎座': {
        'dt_rng': ('1023', '1122'),
        'desc': '天蝎座的人以神秘、热情、坚定著称。他们洞察力强，善于隐藏自己的情感，对事物有深刻的思考。天蝎座的人忠诚、专注，但有时会显得占有欲强或过于敏感。'
        },
    '射手座': {
        'dt_rng': ('1123', '1221'),
        'desc': '射手座的人热爱自由，乐观开朗，喜欢冒险和探索新事物。他们性格直率，善于沟通，但有时会显得缺乏耐心或过于冲动。'
        }
}


def get_xingzuo(date=None, with_desc=False, is_md=False):
    """通过日期获取星座，若is_md=True，则date格式须形如: `0514`"""
    if not is_md:
        date = trans_date(date)
        md = date.strftime('%m%d')
    else:
        md = date
    name_ = None
    for name, info in XINGZUO.items():
        if md >= info['dt_rng'][0] and md <= info['dt_rng'][1]:
            name_ = name
    if name_ is None:
        name_ = '摩羯座'
    if not with_desc:
        return name_
    else:
        return name_, XINGZUO[name_]['desc']

