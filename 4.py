# -*- coding: utf-8 -*-
"""
@author: Andrew Floyd
CS5200 - HW1
Question 4
"""

def altDif(lst):
    #terminating condition
    if len(lst) == 1:
        return lst
    else:
        lst2 = lst[-2:] #take last two elements of list
        value = lst2[0] - lst2[1]
        return altDif(lst[:-2] + [value])
    
l = [3, 5, 4]
alt1 = altDif(l)
print(str(l) + ": " + str(alt1))

l = [6, 7]
alt1 = altDif(l)
print(str(l) + ": " + str(alt1))
        