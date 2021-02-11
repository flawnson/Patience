import random

from typing import *
from logzero import logger

from torch_patience.data.patrons.patron import customer


def source(env, number, interval, counter):
    """Source generates customers randomly"""
    for i in range(number):
        c = customer(env, 'Customer%02d' % i, counter, time_in_bank=12.0)
        env.process(c)
        t = random.expovariate(1.0 / interval)  # Exponential distribution
        yield env.timeout(t)

