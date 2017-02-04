#  coding=utf-8

import re
import pytz


def is_valid_tel(tel):
    if not re.match(r'1\d{10}', tel):
        return False
    return True


def format_time(time):
    return time.astimezone(tz=pytz.timezone('Asia/Shanghai')).strftime('%Y年%m月%d日 %H:%M:%S').decode('utf8')
