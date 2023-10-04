#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('tested.csv')
#read dataset using pandas 


# In[5]:


#look at top of data 
df.head()


# In[ ]:


###Missing value


# In[8]:


df.isnull()
#difficulty in finding for large dataset


# In[9]:


sns.heatmap(df.isnull(),    yticklabels=False,cbar = False,cmap='viridis')


# In[13]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',data=df,hue='Sex',palette='RdBu_r')


# In[16]:


sns.distplot(df['Age'].dropna(),kde=False,color='darkred',bins=40)


# In[18]:


plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=df,palette='winter')


# In[19]:


def age_impute(col):
    Age = col[0]
    Pclass = col[0]
    
    if pd.isnull(Age):
        if Pclass ==1:
            return 42
        elif Pclass ==2:
            return 27
        else :
            return 24
    else:
        return Age


# In[20]:


df['Age'] = df[['Age','Pclass']].apply(age_impute,axis=1)


# In[23]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[25]:


df.drop('Cabin',axis=1,inplace=True)


# In[26]:


df.head()


# In[ ]:




