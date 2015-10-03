# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""
cases = int(input())
for tests in range(cases):
    limits = input()
    limits = limits.split()
    k = int(limits[1])
    number = input()
    larg_product = 0
    instances = [number[i:i+k] for i in range(len(number)-k+1)]
    for k in instances:
        product = 1
        for i in k:
            product *= int(i)
        if product > larg_product:
            larg_product = product
    
    print(larg_product)
