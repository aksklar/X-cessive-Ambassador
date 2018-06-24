
# coding: utf-8

# In[10]:


#this is an easy to use wrapper for The Movie Database
import tmdbsimple as tmdb
tmdb.API_KEY = '7ab58d088ec33774de2b8204f6d3a0eb'


# In[11]:


#these are examples of how to use this wrapper
movie = tmdb.Movies(862)
#gets the keywords of the movie id
response=movie.keywords()


# In[12]:


response


# In[13]:


movie = tmdb.Movies(8844)
response=movie.keywords()


# In[14]:


response


# In[15]:


movie=tmdb.Movies(15602)
response=movie.keywords()


# In[16]:


response


# In[17]:


#so now based off that here's a function
def moviekeywords(movie_id):
    movie=tmdb.Movies(movie_id)
    response = movie.keywords()
    return response


# In[18]:


#tested it out
moviekeywords(862)


# In[19]:


import csv


# In[20]:


import pandas as pd


# In[21]:


#basically read the test file
df=pd.read_csv('test_ml_movies.csv')


# In[22]:


#turned it into a movie list
movie_list=df['tmdbId'].tolist()


# In[29]:


#made a keywords list so that as we loop through the movie id we get the keywords associated with the movie id
keywords=[]
for movie in movie_list:
    keywords.append(moviekeywords(movie))
    
    
    


# In[30]:


print(keywords)


# In[31]:


keywords[0]


# In[32]:


keywords[1]


# In[33]:


keywords[2]

