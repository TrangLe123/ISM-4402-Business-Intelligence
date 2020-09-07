#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns=columns)


# In[8]:


df.to_csv('/Users/Trang Le/OneDrive/Desktop/datasets/studentgrades.csv')


# In[ ]:




