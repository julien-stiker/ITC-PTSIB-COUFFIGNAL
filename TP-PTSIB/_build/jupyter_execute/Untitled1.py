#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lin

get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

np.set_printoptions(precision=3, linewidth=150, suppress=True)


# In[2]:


tab = np.array([[5, 4, 2, 5, 4, 2, 3, 1, 0, 2, 1, 4, 3, 1, 2],
       [5, 3, 1, 3, 4, 0, 3, 2, 1, 0, 2, 2, 2, 0, 1],
       [4, 3, 2, 5, 3, 1, 4, 1, 0, 1, 1, 4, 3, 0, 1],
       [0, 2, 3, 3, 2, 3, 2, 4, 3, 3, 1, 2, 3, 3, 2],
       [1, 2, 2, 4, 3, 1, 4, 3, 1, 1, 0, 1, 2, 2, 3],
       [1, 1, 2, 3, 2, 1, 4, 3, 0, 0, 1, 2, 3, 2, 2]])


# In[3]:


cov = np.cov(tab)

val, vec = lin.eig(cov)
val = val.astype('float')  # on convertit puisqu'on sait que ce sont des réels
print("Valeurs propres de la matrice de covariance :", val,"\n")
print("Vecteurs propres de la matrice de covariance :\n", vec)


# In[4]:


(1/2.383)*cov @ vec[:,1]


# In[5]:


print(vec[:,0])


# In[6]:


vec[:,0]@tab[:,0]


# In[7]:


for i in range(14):
    print(vec[:,0]@tab[:,i])
    


# In[8]:


for i in range(14):
    print(vec[:,1]@tab[:,i])


# In[ ]:




