
# coding: utf-8

# In[18]:


def div(x,y):
    import numpy as np
    x = np.array(x).reshape(1,)
    y = np.array(y).reshape(1,)
    return np.true_divide(x,y)

def test_answer():
    assert div(2,8) != 0

    

