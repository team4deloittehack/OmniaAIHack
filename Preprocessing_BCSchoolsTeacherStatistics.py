#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
pd.set_option('display.max_columns',None)


# In[41]:


df_teach=pd.read_excel("stats.xlsx")


# In[ ]:





# In[37]:


df_teach['TOTAL SALARY'] = pd.to_numeric(df_teach['TOTAL SALARY'], errors='coerce')
df_teach['TOTAL FTE'] = pd.to_numeric(df_teach['TOTAL FTE'], errors='coerce')
df_teach['AVERAGE AGE'] = pd.to_numeric(df_teach['AVERAGE AGE'], errors='coerce')


# In[20]:


df_teach['TOTAL FTE'].dtype


# In[16]:


sal_by_dist=df_teach.groupby('DISTRICT NUMBER')['TOTAL SALARY'].mean()


# In[21]:


fte_by_dist=df_teach.groupby('DISTRICT NUMBER')['TOTAL FTE'].mean()


# In[30]:


count_by_dist=df_teach.groupby('DISTRICT NUMBER')['EDUCATORS CNT'].sum()


# In[38]:


age_by_dist=df_teach.groupby('DISTRICT NUMBER')['AVERAGE AGE'].mean()


# In[48]:


sal_by_dist


# In[53]:


new_table=pd.concat([sal_by_dist,age_by_dist, count_by_dist,fte_by_dist ], axis = 1)


# In[54]:


new_table.to_csv("new_table.csv")


# In[ ]:




