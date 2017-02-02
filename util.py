#  coding=utf-8

import re


def is_valid_tel(tel):
    if not re.match(r'1\d{10}', tel):
        return False
    return True
