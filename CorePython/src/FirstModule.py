'''
Created on 28-Mar-2018

@author: ajitj
'''

def add(a,b):
    return a+b

def addFixedValue(a):
    i = 1
    for i in range(1, 10):
        if i <= 5 :
            print ("smaller number")
        else:
            print ("Larger number")


print (add(1,2))
addFixedValue(1)
