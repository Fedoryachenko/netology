#!/usr/bin/env python
# coding: utf-8

# - Задание 1
# 
# Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
# 
# -оценка 2 и меньше - низкий рейтинг
# 
# -оценка 4 и меньше - средний рейтинг
# 
# -оценка 4.5 и 5 - высокий рейтинг
# 
# Результат классификации запишите в столбец class

# In[12]:


import pandas as pd 


# In[30]:


ratings = pd.read_csv('/Users/anastasiafedoracenko/Desktop/Netology/python/ml-latest-small/ratings.csv')
ratings.head()


# In[41]:


def movies_rating(row):
    if row['rating'] <= 2.0:
        return 'низкий рейтинг'
    elif 2.0<row['rating'] <= 4.0:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'


# In[42]:


ratings['class'] = ratings.apply(movies_rating, axis = 1)
ratings.head()


# - Задание 2
# 
# Используем файл keywords.csv.
# 
# Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определенному региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
# 
# Правила распределения по регионам Центр, Северо-Запад и Дальний Восток.
# 
# 
# Результат классификации запишите в отдельный столбец region.
# 
# 
# 

# In[43]:


geo_data = {

'Центр':['москва', 'тула', 'ярославль'],

'Северо-Запад':['петербург', 'псков', 'мурманск'],

'Дальний Восток':['владивосток', 'сахалин', 'хабаровск'] 
}

towns = []
for values in geo_data.values():
    for i in values:
        towns.append(i)
        
towns


# In[44]:


row = 'мой город москва '

data = row.split(' ')

def check(t):
    for i in t:
        if i in towns:
            for items in geo_data.items():
                if i in items[1]:
                    print(items[0])
check(data)


# In[45]:


df = pd.read_csv('/Users/anastasiafedoracenko/Desktop/Netology/python/ml-latest-small/keywords.csv')
df.head()


# In[54]:


def region_in_keyword(row):
    data = row['keyword'].split(' ')
    i = 0
    for word in data:
        if word in towns:
            for items in geo_data.items():
                if word in items[1]:
                    i += 1
                    return items[0]
    if i == 0:
        return 'undefined'     


# In[55]:


df['region'] = df.apply(region_in_keyword, axis = 1)
df.head()


# In[56]:


df[(df['region'] != 'undefined')]


# In[ ]:





# In[ ]:




