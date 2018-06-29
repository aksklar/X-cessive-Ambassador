
# coding: utf-8

# In[7]:


import omdb


# In[13]:


import pandas as pd


# In[14]:


import csv


# In[15]:


df=pd.read_csv('test_ml_movies.csv')


# In[22]:


movie_list=df['imdbId'].tolist()


# In[40]:


full_plot=[]
for movie in movie_list:
    try:
        res= omdb.request(i='tt00'+str(movie), plot='full',apikey='7329004f')
        data=res.json()
        full_plot.append({"Plot":data['Plot'], "Title":data['Title'],"Year":data['Year']})
    except:
        full_plot


# In[41]:


full_plot


# In[42]:


len(full_plot)


# In[45]:


movie_df=pd.DataFrame(full_plot)


# In[46]:


movie_df


# In[47]:


movie_df.to_csv('movies1_to_49.csv')

