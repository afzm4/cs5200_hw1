# -*- coding: utf-8 -*-
"""
@author: Andrew Floyd
CS5200 - HW1
Question 4
"""

def A(x, y):
    if x == 0:
        return y+1
    elif y == 0:
        return A(x-1, 1)
    else:
        return A(x-1,A(x,y-1))

for i in range(5):
    print(A(i,i))