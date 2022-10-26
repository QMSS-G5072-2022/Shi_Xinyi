#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest


# In[2]:


def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


# In[4]:


@pytest.mark.parametrize("text,expected", [
    ('word','yqtf'),
    ('jesus', 'lguwu'),
    ('AND', 'CPF'),
    ('Dogs are cute', 'Fqiu ctg ewvg'),
])
def test_cipher_looping(text, expected):
    result = cipher(text, shift=2)
    assert result == expected


# In[ ]:




