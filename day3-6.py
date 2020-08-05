# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:13:32 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:29:27 2020

@author: user
"""

d={}

while True:
    print('-----------------')
    print('1.建立辭彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')

    sel=int(input('請輸入指令: '))
      
    if sel ==1:
        while True:
            k1=input('請輸入新單字(0跳出): ')
            
            if k1=='0':
                break
            if k1 not in d:
                g=input('請輸入註解: ')
                d[k1]=g
            else:
                print('已存入')
             
    elif sel ==2:
        for i in d:
            print(i, '是', d[i])
            
    elif sel ==3:
        while True:
           j=input('請輸入想翻譯的字(0跳出)')
           if j == '0':
               break
           if j in d:
               print(d[j])
           else:
               print('這個字不在字典中')
               
        
        
     #elif sel ==4:
       
  #  elif sel ==5:
        
   # else:
     #   print('已離開')
     #   break