# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:29:27 2020

@author: user
"""

while True:
    print('-----------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    
    sel=int(input('請輸入指令: '))
      
    if sel ==1:
        k1=int(input('請輸入數字1: '))
        k2=int(input('請輸入數字2: '))        
        print(k1, '+', k2, '=', k1+k2)
    
    elif sel ==2:
        k1=int(input('請輸入數字1: '))
        k2=int(input('請輸入數字2: '))        
        print(k1, '-', k2, '=', k1-k2)
    
    elif sel ==3:
        k1=int(input('請輸入數字1: '))
        k2=int(input('請輸入數字2: ')) 
        print(k1,"x",k2, "=" ,k1*k2)
     
    elif sel ==4:
        k1=int(input('請輸入數字1: '))
        k2=int(input('請輸入數字2: '))        
        print(k1, '/', k2, '=', k1/k2)
    
    else:
        print('結束')
        break
