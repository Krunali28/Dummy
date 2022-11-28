#!/usr/bin/env python
# coding: utf-8

# In[1]:


# floor division  --  //
# it will round off output to nearest smallest integer


# In[2]:


11/3


# In[3]:


11%3


# In[4]:


11//3


# In[5]:


# 1 2 3 3.66 4 5 6


# In[8]:


-11//3


# In[9]:


#-4 -3.66 -3 -2 -1 0 1 2 3


# In[10]:


# logical operators
# AND, OR, NOT


# In[11]:


# TO CHECK GRADE IF STUDENT USING HIS MARKS
# 90 >  A
# 80 TO 90  B   MARKS>80 , MARKS <90
# 60 TO 80  C    MARKS >60 , MARKS <80


# In[12]:


# AND 
# TRUE AND TRUE  - TRUE
# TRUE AND FALSE - FALSE
# FALSE AND TRUE - FALSE 
# FALSE AND FALSE - FALSE

# OR
# TRUE OR TRUE  - TRUE
# TRUE OR FALSE - TRUE
# FALSE OR TRUE - TRUE
# FALSE OR FALSE- FALSE


# In[13]:


# COMPARISION OPERATORS
# equal to     --       ==
# less than    --        <
# greater than --        >
# lessthan or equal to-- <=
# greater than or equal to--  >=
# not equal to --         !=


# In[17]:


# assignment operators
#a=a+1      a+=1
#a=a-1      a-=1
#a=a*2      a*=2
#a=a/2      a/=2


# In[19]:


# membership operators
# in, not in 


# In[20]:


# list - will store more than one vale at a time
a=[1,2,3,4,5]


# In[21]:


type(a)


# In[22]:


a=[1,2,3,4,5]


# In[23]:


1 in a


# In[24]:


6 in a


# In[25]:


1 not in a


# In[26]:


6 not in a


# # user input method

# In[ ]:


#syntax - by using input method
# variable_name=input("message")
# if datatype is not given the by default it will be of string type.


# In[34]:


a=input("enter value of a:")
b=input("enter value of b:")
c=a+b


# In[35]:


c


# In[36]:


"hello"+"world"


# In[37]:


"2"+"3"


# In[38]:


# str to int  -- int(str)
# int to float - float(int)


# In[39]:


a="2"


# In[46]:


a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=a+b


# In[48]:


a=input("enter value of a:")
b=input("enter value of b:")
c=int(a+b)


# In[51]:


print("addition is",c)


# In[50]:


type(c)


# In[ ]:




