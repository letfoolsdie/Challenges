# -*- coding: utf-8 -*-
"""
@author: Nikolay_Semyachkin
"""
cases = int(input())
n_array = []
for i in range(cases):
    n = int(input())
    n_array.append(n)#print('case#', i)
for i in n_array:    
    sum_of_squares = (i**3)/3 + (i**2)/2 + i/6
    square_sum = (i*(i+1)/2)**2
    print(abs(int(sum_of_squares - square_sum)))
