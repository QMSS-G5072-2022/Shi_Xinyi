#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pytest

def cipher(text, shift, encrypt=True):
    assert type(shift) is int, 'Shift should be an integer'
        
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


def test_cipher_word():
    text = 'word'
    shift = 2
    expected = 'yqtf'
    actual = cipher(text, shift)
    assert actual == expected


def test_cipher_shift():
    text = 'word'
    shift = -1
    expected = 'vnqc'
    actual = cipher(text, shift)
    assert actual == expected


def test_cipher_symbol():
    text = 'word!'
    shift = -1
    expected = 'vnqc!'
    actual = cipher(text, shift)
    assert actual == expected 

def test_cipher_integer():
    
    text = 'word'
    shift = "two"
    expected = 'yqtf'
    with pytest.raises(AssertionError):
        cipher(text, shift)

