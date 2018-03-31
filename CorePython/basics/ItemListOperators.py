'''
Created on 29-Mar-2018

@author: ajitj
'''
# Python code to demonstrate working of 
# setitem(), delitem() and getitem()
 
# importing operator module 
import operator
 
# Initializing list
li = [1, 5, 6, 7.23, "ajit"]
 
# printing original list 
print ("The original list is : ")
for i in range(0,len(li)):
    print (li[i]),
 
print ("\r")
 
# using setitem() to assign 3 at 4th position
operator.setitem(li,3,3)
 
# printing modified list after setitem()
print ("The modified list after setitem() is : ")
for i in range (0,len(li)):
    print(li[i]),
 
print ("\r")
 
# using delitem() to delete value at 2nd index
operator.delitem(li,1)
 
# printing modified list after delitem()
print ("The modified list after delitem() is : ")
for i in range(0,len(li)):
    print (li[i]),
 
print ("\r")
 
# using getitem() to access 4th element
print ("The 4th element of list is : ")
print (operator.getitem(li,3))