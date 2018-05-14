
# coding: utf-8

# In[8]:


AcadGild = [letter for letter in 'ACADGILD']
print(AcadGild)


# In[23]:


my_list = []

for s in ["x", "y", "z"]:
    my_list.append(s*1), my_list.append(s*2), my_list.append(s*3), my_list.append(s*4)

print(my_list)


# In[36]:


my_list = []

for s in ("x"),("y"),("z"):
    my_list.append(s*1), 
    
for s in ("x"),("y"),("z"):
    my_list.append(s*2),

for s in ("x"),("y"),("z"):
    my_list.append(s*4), 
    
print(my_list)


# In[47]:


my_list = []

for s1 in ["2"],["3"],["4"]:
    my_list.append(s1),
for s2 in ["3"],["4"],["5"]:
    my_list.append(s2),
for s3 in ["4"],["5"],["6"]:
    my_list.append(s3),
        
print(my_list)


# In[70]:


my_list = []

for s1 in [[2, 3, 4, 5]]:
    my_list.append(s1),
for s2 in [[3, 4, 5, 6]]:
    my_list.append(s2),
for s3 in [[4, 5, 6, 7]]:
    my_list.append(s3),
for s4 in [[5, 6, 7, 8]]:
    my_list.append(s4),
        
print(my_list)


# In[83]:


my_list = [(x,y) for x in [1, 2, 3] for y in [1, 2, 3]]
print(my_list)

