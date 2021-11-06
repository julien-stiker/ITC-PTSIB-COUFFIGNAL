#!/usr/bin/env python
# coding: utf-8

# 

# # TP2 : Des modules, des tests et un peu de complexité
# 
# 
# ```{note}
# :class: dropdown
# The note body will be hidden!
# ```
# 
# ## Les modules
# 
# ```{adomition} Solution
# :class: dropdown, tip
# The note body will be hidden!
# ```
# 
# ```{math}
# :label: my-math-ref
# w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
# ```
# 
# $$
#   \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
# $$
# 
# 

# ```{code-cell} ipython3
# :tags: [remove-stderr]
# 
# import sys
# print("this is some stdout")
# print("this is some stderr", file=sys.stderr)
# ```

# In[1]:


def essai(a, b ):
    return 2


# In[2]:


from cowpy import cow
cheese = cow.Moose()
msg = cheese.milk("Welcome Bob!")
print(msg)


# 

# 

# In[ ]:




