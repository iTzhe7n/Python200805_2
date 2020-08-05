# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:38:30 2020

@author: AE401
"""
s=list()

def av(scores):             #平均的finction
    total=0
    for i in scores:
        total=total+i
    return total/p

'''main function'''

p=int(input('請輸入人數'))
for i in range(p): 
    a=int(input('成績'))
    s.append(a)
    
AV=av(s)
print('平均: ' , AV)

