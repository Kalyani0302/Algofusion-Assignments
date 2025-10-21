#!/usr/bin/env python
# coding: utf-8

# In[12]:
#lhguyijknbb
#rgyhikjhg


#list methods
l=[11,22,33,44,55]

#append
l.append(66)
print(l)


# In[13]:


#copy

m=l.copy()
m


# In[15]:


#count
l1=[11,22,33,44,55,11,11,22]
l1.count(11)


# In[19]:


a=['K','A','L','Y','A','N','I']
B=['P','A','D','A','L','A']
a.extend(a)
print(a)
print()
c=[1,2,3,4,5]
d=[6,7,8,9,10]
c.extend(d)
print(c)


# In[9]:


#clear
m.clear()
print(m)
l.clear()


# In[20]:


a=[11,22,33,44]
a.pop()
print(a)
a.pop(1)
print(a)


# In[21]:


a.remove(11)


# In[22]:


print(a)


# In[14]:


b=[1,2,3,4,5]
max(b)


# In[15]:


min(b)


# In[4]:


l=[88,99,77,22,99]
l.sort()
print(l)


# In[5]:


#index
x=l.index(99)
print(x)


# In[6]:


list1=[1,2,3,4,5]
list1.reverse()
print(list1)


# In[1]:


#dictionary methods - pop,popitem,clear,get,items,key,values,copy,fromkeys,update,setdefault


# In[17]:


d1={"name":"kalyani","lname":"medam","course":"bTech","branch":"ece",}

d1.pop("course")


# In[18]:


print(d1)


# In[19]:


d1.popitem()


# In[20]:


print(d1)


# In[6]:


d1.clear()


# In[7]:


print(d1)


# In[10]:


d2={"a":2,"b":4,"c":6,1:8,2:10}


# In[11]:


d2.get("a") #returns the mentioned key in get()


# In[12]:


print(d1)


# In[15]:


d2={"a":2,"b":4,"c":6,2:10}


# In[16]:


d2.get("a") #returns the mentioned key in get()


# In[17]:


d2.keys()


# In[18]:


d2.values()


# In[19]:


d2.items()


# In[20]:


d3=d2.copy()


# In[21]:


{'a':2,'b':4,'c':6,1: 8, 2: 10}


# In[22]:


d3.update({"a":"kalyani"})


# In[23]:


d2.keys()


# In[27]:


d2.values()


# In[28]:


d2.items()


# In[29]:


d3=d2.copy()


# In[30]:


print(d3)


# In[31]:


d3.update({"a":"kalyani"})


# In[32]:


d3


# In[ ]:




