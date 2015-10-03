# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""

cases = int(input())
for i in range(cases):
    n = int(input())
    f1 = 1
    f2 = 1
    fn = 0
    total = 0
    
    while fn < n:
        if fn % 2 ==0:
            total += fn
        fn = f1 + f2
        f1 = f2
        f2 = fn
    print(total)