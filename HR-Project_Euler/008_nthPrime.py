# -*- coding: utf-8 -*-
"""

@author: Nikolay_Semyachkin
"""
import math
def nthPrime(n):
    primes = [2]
    num = 3
    while (len(primes)<n):
        for i in primes:
            isPrime = True
            if i > math.sqrt(num):
                break
            if num%i == 0:
                isPrime=False
                break
        if isPrime == True:
            primes.append(num)
        num += 2
    return(primes)

tests = int(input())
primes = nthPrime(10000)
for t in range(tests):
    n = int(input())
    print(primes[n-1])
    
    