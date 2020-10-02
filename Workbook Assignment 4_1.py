#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/Trang Le/OneDrive/Desktop/datasets/gradedata.csv" 
df = pd.read_csv(Location) 
df.head()


# In[12]:


import numpy as np
df['Timemgnt'] = np.where((df['exercise']>3) & (df['hours']>17), 'Busy', 'Not busy')
df.tail(10)


# In[ ]:




