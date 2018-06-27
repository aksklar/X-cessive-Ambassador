
# coding: utf-8

# In[1]:


import requests
import json


# In[2]:


# New Dependency! Use this to pretty print the JSON
# https://docs.python.org/3/library/pprint.html
from pprint import pprint


# In[17]:


# Note that the ?t= is a query param for the t-itle of the
# movie we want to search for.
url = "http://www.omdbapi.com/?i="
api_key = "&apikey=7329004f"


# In[32]:


# Performing a GET request similar to the one we executed
# earlier
response = requests.get(url + "tt0114709" + api_key + "plot=full")
print(response.url)


# In[19]:


# Converting the response to JSON, and printing the result.
data = response.json()
pprint(data)


# In[20]:


# Print a few keys from the response JSON.
print(f"Movie was directed by {data['Director']}.")
print(f"Movie was released in {data['Country']}.")


# In[21]:


import omdb


# In[36]:


res= omdb.request(i='tt0114709', plot='full',apikey='7329004f')
print(res)


# In[37]:


pprint(res.json())


# In[29]:


data=res.json()


# In[30]:


pprint(data)


# In[31]:


data['Plot']


# In[38]:


import pandas as pd

