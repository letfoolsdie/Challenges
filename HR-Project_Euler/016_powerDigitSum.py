# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""
cases = int(input())
for i in range(cases):
    power = int(input())
    number = 2**power
    num_str = str(number)
    digitsum = 0
    for k in num_str:
        digitsum += int(k)
    print(digitsum)
