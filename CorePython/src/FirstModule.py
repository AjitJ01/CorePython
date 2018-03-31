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
            print 'Smaller or equal than 5.\n',
        else:
            print 'Larger than 5.\n',


print add(1,2)
addFixedValue(1)
