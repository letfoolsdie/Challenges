# -*- coding: utf-8 -*-
"""
@author: Nikolay_Semyachkin
"""

import math

cases = int(input())
for i in range(cases):
    n = int(input())
    n = str(math.factorial(n))
    digsum = 0
    for l in n:
        digsum += int(l)
    print(digsum)