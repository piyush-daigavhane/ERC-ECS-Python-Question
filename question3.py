#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Create a function which takes a string as an input and generates a dictionary 
#with each word as a key and its corresponding count(number of times the word occurs in the string) as a value.


a=input("enter a string :")
b=a.split()
c=[]
d=[]
for element in b:
    if element not in c:
            c.append(element)
            e=b.count(element)
            d.append(e)
e = dict(zip(c,d))
print(e)


# In[ ]:





# In[ ]:




