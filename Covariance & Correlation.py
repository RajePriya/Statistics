#!/usr/bin/env python
# coding: utf-8

# ## covariance & Correlation with Python

# In[1]:


import seaborn as sns


# In[7]:


df=sns.load_dataset('healthexp')
df.head()


# In[8]:


## Covariance
import numpy as np


# In[9]:


df.cov()


# In[10]:


## Spearman ranking Correlation
df.corr(method='spearman')


# In[11]:


## Pearson Correlation
df.corr(method='pearson')


# In[12]:


df=sns.load_dataset('penguins')
df.corr()


# In[ ]:




