#!/usr/bin/env python
# coding: utf-8

# In[34]:


#From a given list, create a list of all unique elements.


# In[35]:


a=[1,2,3,4,5,6,7,3,4,5,2,34,5,5,6,2]
b=[]
for element in a:
    if element not in b:
        b.append(element)
print(b)


# In[ ]:




