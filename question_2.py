#!/usr/bin/env python
# coding: utf-8

# In[8]:


def quadratic(equation):
        e=equation.split()
        a=int(e[0])
        b=int(e[2])
        c=int(e[4])
        s=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
        h=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
        d=[s,h]
        print(d)

equation=(input("enter the equation in the form <sign>a_*x^2_<sign>b_*x_<sign>c incorporating signs of a,b,c :"))
quadratic(equation)


# In[ ]:





# In[ ]:




