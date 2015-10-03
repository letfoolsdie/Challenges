# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""
def small_number(n):
    if n == 1:
        return n
    else:
        divs = [i for i in range(n, 0, -1)]
        inc = small_number(n-1)
        number = inc
        
        while not all([number % i == 0 for i in divs]):
            number += inc
        return number
        
cases = int(input())
for i in range(cases):
    test = int(input())
    print(small_number(test))
