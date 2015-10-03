# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""
def check(num):
    num = int(num)
    for i in range(100,999):
        if num % i == 0:
            if len(str(int(num/i))) == 3 and len(str(int(num/(num/i)))) == 3:
#                print(num/i, num/(num/i))
                return True

cases = int(input())
for tests in range(cases):
    N = input()
    for i in range(int(N), 10000, -1):
        if str(i) == str(i)[::-1]:
            if check(i):
                print(i)
                break
