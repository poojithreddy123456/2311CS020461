#!/usr/bin/env python
# coding: utf-8

# In[36]:


d={ 101: 4, 102: 7,'B':2}
d


# In[37]:


d['B']


# In[38]:


d[101] #dict allow duplicate keys


# In[39]:


d


# In[40]:


d[105]=5000
d


# In[41]:


d[101]=9
d.get(102)


# In[42]:


d.update({101:'India'})
d


# In[43]:


d.update({106:'India'}) #dictioary allow duplicate keys
d


# In[44]:


d


# In[45]:


d.get(105)


# In[46]:


d.keys()


# In[47]:


d.values()


# In[48]:


d.items()


# In[49]:


d


# In[50]:


d[104]=[1000,5000,6000,7000]


# In[51]:


# d.update({104:[1000,5000,6000,7000]})


# In[52]:


d


# In[53]:


d[104]


# In[54]:


type(d[104])


# In[55]:


d


# In[56]:


type(d)


# In[58]:


d[101]={50:[7,8,9,10],'apple':(20,10,70,[90,180,270])}
d


# In[ ]:





# In[59]:


d[105]={'a':{30,50,70},'b':(1000,5000,7000,9000),'c':['k',{'L':[11,22],'M':(77,88)},'N']}
d


# In[60]:


wap to know number is positive negative or zero


# In[61]:


x=-6
if x>0:
    print('pos')
elif x<0:
    print('neg')
else:
    print('zero')


# In[62]:


y=9
if y+6>5:
    print('M')
elif y>4:
    print('k')
elif y>7:
    print('H')
else:
    print('0')


# In[63]:



y=1
if y>5:
    print('M')
elif y>4:
    print('k')
elif y>7:
    print('H')
else:
    print('o')


# In[80]:


x='Telangana'
if [x]=='t' or x[0]=='T' :
    print('Yes')
else:
    print('No')


# In[77]:


y='india123'
y


# In[82]:


x='Tiger'
if [x]=='T' or x[0]=='t' :
    print('No')
else:
    print('Yes')


# In[84]:


x='Tiger'
if x[0]=='h' or x[0]=='H' :
    print('Yes')
else:
    print('No')


# In[85]:


if x[0]=='s' or x[0]=='S' or x[0]=='m' or x[0]=='M' or x[0]=='h' or x[0]=='h':
    print('Yes')
else:
    print('NO')


# In[ ]:




