#  coding=utf-8
from rest_framework.throttling import AnonRateThrottle


class FixRateThrottle(AnonRateThrottle):
    scope = 'fix'
    rate = '1/minute'
