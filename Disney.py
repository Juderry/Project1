#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
import pandas as pd


# In[68]:


#Disney Data

disney_data = pd.read_csv("/Users/Judy/Downloads/disney_movies_total_gross.csv")
print ("Disney Data Loaded Successfully!")
print (disney_data)


# In[69]:


disney_data.head()


# In[70]:


disney_data.info()


# In[71]:


disney_data['genre'].value_counts()


# In[72]:


disney_data['mpaa_rating'].value_counts()


# In[73]:


new_name = {'movie_title' : 'Movie Title', "release_date" : 'Release Date', 'genre' : 'Genre', 'mpaa_rating' : 'MPAA Rating', 'total_gross' : 'Total Gross', 'inflation_adjusted_gross' : 'Inflation Adjusted Gross'}

disney_data.rename(columns= new_name, inplace=True)
disney_data.head()


# In[ ]:


#Question 1. A MPAA Rating of G has a greater gross revenue with inflation over other MPAA Ratings.


# In[74]:


df = pd.read_csv("/Users/Judy/Downloads/disney_movies_total_gross.csv")
print(df)


# In[75]:


value_list = ["G"]
boolean_series = df.mpaa_rating.isin(value_list)
filtered_df = df[boolean_series]

print(filtered_df)


# In[76]:


filtered_df['inflation_adjusted_gross'].mean()


# In[77]:


value_list = ["PG","PG-13","R"]
boolean_series = df.mpaa_rating.isin(value_list)
filteredrat_df = df[boolean_series]

print(filteredrat_df)


# In[78]:


filteredrat_df['inflation_adjusted_gross'].mean()


# In[ ]:


#Answer: True, G rating result in $291,260,995 vs Non-G rating result $91,145,127 with adjustment for inflation


# In[ ]:


#Question 2. Highest Grossing Films are within the Comedy Genre


# In[23]:


df = pd.read_csv("/Users/Judy/Downloads/disney_movies.csv")
print(df)


# In[80]:


#value_list = ["Comedy"]
#boolean_series = df.genre.isin(value_list)
#filteredgenre_df = df[boolean_series]

#print(filteredgenre_df)

grouped_df = df.groupby("genre")
mean_df = grouped_df.mean()
mean_df = mean_df.reset_index()
pd.options.display.float_format = '{:20,.2f}'.format

print(mean_df)


# In[89]:


import matplotlib.pyplot as plt

grouped_df = df.groupby("genre")
mean_df = grouped_df.mean()
mean_df = mean_df.reset_index()
pd.options.display.float_format = '{:20,.2f}'.format

plt.figure(figsize=(20,10))
plt.bar(df['genre'],df['total_gross'])
plt.title('Disney Movie Gross by Genre')
plt.xlabel('Genre')
plt.ylabel('Total Gross')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#Answer - False, Comedy gross is 44,613,295 vs  greatest gross is for adventure at 127,047,050


# In[100]:


#Question 3. 
#Disney Films Released before 01-01-1984 have a lower gross per film compared to those released during and after


# In[91]:


df = pd.read_csv("/Users/Judy/Downloads/disney_movies_total_gross.csv")
print(df)


# In[93]:


df = pd.read_csv("/Users/Judy/Downloads/disney_movies_total_gross.csv")
df['Dates'] = pd.to_datetime(df['release_date']).dt.date

filtereddate_df = df.loc[(df['release_date'] >= '1937-01-01')
                     & (df['release_date'] < '1984-01-01')]

print(filtereddate_df)


# In[94]:


filtereddate_df['inflation_adjusted_gross'].mean()


# In[96]:


df = pd.read_csv("/Users/Judy/Downloads/disney_movies_total_gross.csv")
df['Dates'] = pd.to_datetime(df['release_date']).dt.date

filteredinvdate_df = df.loc[(df['release_date'] >= '1984-01-01')
                     & (df['release_date'] < '2021-01-01')]

print(filteredinvdate_df)


# In[97]:


filteredinvdate_df['inflation_adjusted_gross'].mean()


# In[ ]:


#Answer - False, Before 01-01-1984 = $483,192,618 and After 01-01-1984 = $93,884,454

