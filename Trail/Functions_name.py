#!/usr/bin/env python
# coding: utf-8

# ## Functions:
# When a set of code is repeated multiple times then we can put it under funciton and call whenever required
# updation or debugging is easier as changes made once will be impacted in all places
# Function need to be created first in the coding then only we can call
# function can be used from one phyton code to another
# def funcitonname(args1):
# """ this will retun information about the funciton as Docstring"""
#    statement1
#    statement2
#    value =---
#    return value #if return is not used then the funciton wont return any values
#    
# ### Function calling 
# functionname(args2) #if we use shift tab to understand the fucntion then the multiline comment next to the function will display as Docstring
# 
# function inside a class is called methods
# function inside a python file is called module
# 
# Whenever we declare a function,it will not be compiled by the compiler instead it will be just saved in a memory space ,only when we call the funciton, it will start compiling.However syntax error alone will be notified.In general when we declare a funciton it doesnot mean tat it runs.Only when we call the funciton then we can understand
# 

# ## Types of Arguments
# args1->formal argument->for reference we use this while declaration
# args2->actual argument->original value that we are passing to the funciton
# 
# #### Positional Arguments:
# In formal and Actual arguments we need to provide same number of arguments and also we need to mention the values in correct position
# ex in below area_circle example ,passsing values in wrong position will return wrong output
# 
# #### Keyword Arguments:
# In formal and Actual arguments we need to provide same number of arguments and also we need to mention the values in different position by we need to explicitly mention argument name
# 
# #### Default Arguments:
# If we fail to send Actual arguments then the default argument declared in formal arguments will be taken.here passing value for default argument is optional
# 
# #### Variable Length Arguments:
# here in syntax we use * .and in actual we will be passing a multi valued tuple or list as arguments.Based on how many variables we are declaring in formal arguments.actual will be adjusted
# values after * will be considered as tuples
# 

# In[39]:


#positional Arguments
def areacircle(r,p):
    return p*r*r

print(areacircle(10,3.14))
print(areacircle(3.14,10))
#print(areacircle(10,3.14,99)) will throw error as number of arguments not matching

#Keyword Arguments
def areacircle(r,p):
    return p*r*r

print(areacircle(10,3.14))
print(areacircle(p=3.14,r=10))
#print(areacircle(r=10,p=3.14,99)) will throw error as number of arguments not matching

#Default Arguments
def areacircle(r,p=3.14):
    return p*r*r

print(areacircle(10))
print(areacircle(p=3.14,r=10))
print(areacircle(10,3.14))
print(areacircle(10,10))
#print(areacircle(r=10,p=3.14,99)) will throw error as number of arguments not matching

#variablelength Arguments
def totalsum1(a,*b):
    first=a
    total=0
    print(b,type(b))
    for i in b:       
        total=total + i
        
    return total

def totalsum2(a,b,*c):
    first=a
    second=b
    total=0
    print(c,type(c))
    for i in c:       
        total=total + i
        
    return total
    
print(totalsum1(1,2,3,4,5))
print(totalsum2(1,2,3,4,5,6,7))


# ## Type of variable
# Global Variable
# These variables have scope inside the entire Python Program
# You can use the keyword global to use that variable across anywhere
# even if a variable is declared inside a function using the word global it will be considered as global variable
# 
# Local Variable
# These variables have scope inside the FUNCTION only

# In[ ]:


#function without argument
def add():
    num1=int(input("Provide first number:"))
    num2=int(input("Provide second number:"))
    result=num1+num2
    print(f"sum of number {result}")

for i in range(0,5):
    add()


# In[41]:


pen="red"
pen1="blue"
def color():
    pen="yellow" # this will be used only when function is called,rest time 
    print(pen)
    print(pen1)
    global pen2
    pen2="blue"#global declaration
    
print(pen)
color()
print(pen)
print(pen2)


# In[1]:


def color():
    pen="yellow" # this will be used only when function is called,rest time global variable will be considered.As this pen dont have global declaration it will throw error
    print(pen)
    
print(pen)
color()
print(pen)


# In[11]:


#function with argument
def add(num1,num2):
    result=num1+num2
    print(f"sum of number {result}")
    return result

for i in range(0,5):
    returnedval=add(i,i+1)
    print(f"returned value {returnedval}")
  


# In[16]:


#function with argument
def operation(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return add,sub,div

for i in range(0,5):
    add1,sub1,div1=operation(i,i+1)
    operation1=operation(i+1,i+2)
    print(f"Addition value {add1}",type(add1))
    print(f"operation value {operation1}",type(operation1))
  


# In[ ]:





# In[ ]:





# In[ ]:




