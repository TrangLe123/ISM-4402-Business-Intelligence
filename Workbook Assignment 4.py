#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/Trang Le/OneDrive/Desktop/datasets/gradedata.csv" 
df = pd.read_csv(Location) 
df.head()


# In[3]:


bins = [0, 80, 100]
groups_name = ['Fail', 'Pass']
df['MasterProgram'] = pd.cut(df['grade'], bins, labels = groups_name)
df.head()


# In[4]:


pd.value_counts(df['MasterProgram'])


# In[ ]:




