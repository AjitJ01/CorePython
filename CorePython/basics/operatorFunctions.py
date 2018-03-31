'''
Created on 28-Mar-2018

@author: ajitj
'''
# Python code to demonstrate working of 
# add(), sub(), mul()
 
# importing operator module 
import operator
 
# Initializing variables
a = 4
b = 3
c = 10
 
# using add() to add two numbers
print ("The addition of numbers is :");
print (operator.add(operator.add(a, b), c))
 
# using sub() to subtract two numbers
print ("The difference of numbers is :");
print (operator.sub(b, a))
 
# using mul() to multiply two numbers
print ("The product of numbers is :");
print (operator.mul(a, b))

#Extra operators
# using truediv() to divide two numbers
print ("The true division of numbers is : ");
print (operator.truediv(a,b))
 
# using floordiv() to divide two numbers
print ("The floor division of numbers is : ");
print (operator.floordiv(a,b))
 
# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ");
print (operator.pow(a,b))
 
# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ");
print (str(operator.mod(b,a))+"\n-----------------------------")

# using lt() to check if a is less than b
if(operator.lt(a,b)):
    print ("3 is less than 3")
else : print ("3 is not less than 3")
 
# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
    print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")
 
# using eq() to check if a is equal to b
if (operator.eq(a,b)):
    print ("3 is equal to 3")
else : print ("3 is not equal to 3")

print("--------------------------------------")

# using gt() to check if a is greater than b
if (operator.gt(a,b)):
    print ("4 is greater than 3")
else : print ("4 is not greater than 3")
 
# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
    print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")
 
# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
    print ("4 is not equal to 3")
else : print ("4 is equal to 3")




