#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import folium as fo
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


map = fo.Map()


# In[4]:


map


# In[5]:


x = fo.FeatureGroup(name='My Map')


# In[6]:


x.add_child(fo.Marker(location=[27.1750,78.0422] , popup='hey' , icon=fo.Icon(color='blue')))


# In[7]:


map.add_child(x)


# In[8]:




for lat,lon in ([34,53],[24,-50],[90,-68]):
    x.add_child(fo.Marker(location=[lat,lon] ,
                          popup='hey' , icon=fo.Icon(color='red')))


# In[9]:




map.add_child(x)


# In[11]:


volcano = pd.read_csv('volcano.csv')


# In[12]:


lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])


# In[13]:


vol = fo.FeatureGroup(name='My Map')


# In[14]:


for lat,lon,name in zip(lat_vo,lon_vo,name_vo):
    vol.add_child(fo.Marker(location=[lat,lon] ,
                          popup=name , icon=fo.Icon(color='red')))


# In[15]:


map.add_child(vol)


# In[16]:


vol.add_child(fo.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))


# In[17]:




map.add_child(vol)


# In[23]:


popu = pd.read_csv('us_cities_pop.csv')


# In[24]:


popu.head()


# In[25]:


lat_po = list(popu['lat'])
lon_po = list(popu['lon'])
name_po = list(popu['name'])
pop_po = list(popu['pop'])


# In[26]:


po = fo.FeatureGroup(name='My Map')


# In[27]:


def mar(popu):
    if(popu>35000):
        return 'red'
    elif(popu>10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'


# In[28]:


for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name] , 
                          icon=fo.Icon(color=mar(pop))))


# In[29]:


map.add_child(po)


# In[ ]:




