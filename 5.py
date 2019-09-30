# -*- coding: utf-8 -*-
"""
@author: Andrew Floyd
CS5200 - HW1
Question 4
"""

def f35q(n):
    if n < 8:
        return "Error"
    elif n%5 == 0:
        return (n/5, 0)
    elif n%5 == 1:
        return ((n-6)/5, 2)
    elif n%5 == 2:
        return ((n-12)/5, 4)
    elif n%5 == 3:
        return ((n-3)/5, 1)
    else:
        return ((n-9)/5, 3)
    
print("(# of 5's, # of 3's):")
for i in range(7, 100):
     print(str(i) + ": " + str(f35q(i)))
