# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:49:54 2020

@author: Saptarshi
"""

import math
arr =[]

test = int(input())
for i in range(test):
    
    #finding the probabilty
    N,T,M = map(int,input().split())
    c = math.factorial(N-M)
    b = math.factorial(T)
    a = math.factorial(N-M-T)
    prob = 1 - (c)/(b*c)
    
    #finding in fraction form
    p,q = (prob).as_integer_ratio()
    
    #finding multiplicative inverse
    m =1000000007
    y = pow(q,m-2,m)

    arr.append(y)

for i in range(test):
    print(arr[i])
