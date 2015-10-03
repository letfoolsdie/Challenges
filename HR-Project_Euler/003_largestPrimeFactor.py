# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""

import math

def largest_factor(N):    
    for i in range(2, int(math.sqrt(N) + 1)):
        if N % i == 0:
            N //= i
            return largest_factor(N)
    return N

cases = int(input())
for tests in range(cases):
    N = int(input())
    largest = largest_factor(N)
    print(largest)