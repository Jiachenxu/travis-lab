
# coding: utf-8

# In[12]:


def test_charnum():
    f = open("input.txt", "r", encoding = 'utf-8')
    char = f.read().strip()
    assert len(char) == 6

