# -*- coding: utf-8 -*-
"""
@author: Nikolay_Semyachkin
"""
import math

n = int(input())

result = 0
for i in range(10, n):
    s = str(i)
    product = 0
    for u in s:
        product += math.factorial(int(u))
    if product % i == 0:
        result += i
        
print(result)
