# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""

def sumof3b(n):
    n = (n-1)//3
    return (6+3*(n-1))*n//2

def sumof5b(n):
    n = (n-1)//5
    return (10+5*(n-1))*n//2

def sumof15b(n):
    n = (n-1)//15
    return (30+15*(n-1))*n//2

cases = int(input())
for i in range(cases):
    n = int(input())    
    print(sumof3b(n) + sumof5b(n) - sumof15b(n))