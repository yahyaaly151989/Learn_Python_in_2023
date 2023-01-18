#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {'weight':[300, 250, 800],
        'price':[3, 2, 5]}

df = pd.DataFrame(data)

print(df)


# In[2]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

standardized_data = scaler.fit_transform(df)

print(standardized_data)


# In[3]:


standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

print(standardized_df)


# How to normalize data in Python

# In[4]:


import pandas as pd

data = {'weight':[300, 250, 800],
        'price':[3, 2, 5]}

df = pd.DataFrame(data)

print(df)


# In[5]:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(df)

print(normalized_data)


# In[6]:


normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print(normalized_df)


# In[ ]:




