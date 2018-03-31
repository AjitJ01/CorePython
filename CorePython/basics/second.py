'''
Created on 29-Mar-2018

@author: ajitj
'''

str = "Ajit Jadhav"
str= str[::-1]
newStr = list(str)
newStr.reverse()
newStr  = "".join(newStr)
print(newStr)
