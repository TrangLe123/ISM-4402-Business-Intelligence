#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
from sqlalchemy import create_engine

db_file = r'salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))
sql = "select name from sqlite_master where type = 'table'"
sale_data_df = pd.read_sql(sql, engine)
sale_data_df


# In[27]:


import pandas as pd
from sqlalchemy import create_engine

db_file = r'salesdata.db' 
engine = create_engine(r"sqlite:///{}".format(db_file)) 
sql = 'SELECT * from scores;'
sales_data_df = pd.read_sql(sql, engine) 
sales_data_df.head() 


# In[ ]:





# In[ ]:




