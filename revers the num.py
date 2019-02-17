# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:36:30 2017

@author: lenovo
"""

def ReversNum(num):
    '''return the reverse of the given number
    >>>12345
    54321
    '''
    num = num * 10
    nDigits = 0
    i = 10
    while (num//i) > 10:
        i = i * 10
        nDigits = nDigits + 1
        
    list1 = []
    
    while num >= 10:
        res1 = num // 10**nDigits
        res2 = num % 10**nDigits
        list1.append(res1)
        num = res2
        nDigits = nDigits -2
    list1.append(res2)
    
    list2 = []
    for index in range(len(list1)):
        num1 = list1[index] // 10
        num2 = list1[index] % 10
        result = num1 - num2
        list2.append(list1[index] - (result * 9))
    
    
    list3 = []
    power = 0
    for index in range(len(list2)):
        list3.append(list2[index]*(10**power))
        power = power + 2
        
    summation = 0
    for index in range(len(list3)):
        summation = summation + list3[index]
    return print(summation) 
        
def Entery():
    number = int(input('Enter the Number that you would like to make it reversed : '))
    return ReversNum(number)
        
   
Entery()
    
