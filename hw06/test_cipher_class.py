#!/usr/bin/env python
# coding: utf-8

# In[ ]:
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

class TestClass:

    def test_cipher_word(self):
        text = 'word'
        shift = 2
        expected = 'yqtf'
        actual = cipher(text, shift)
        assert actual == expected


    def test_cipher_shift(self):
        text = 'word'
        shift = -1
        expected = 'vnqc'
        actual = cipher(text, shift)
        assert actual == expected


    def test_cipher_symbol(self):
        text = 'word!'
        shift = -1
        expected = 'vnqc!'
        actual = cipher(text, shift)
        assert actual == expected 

    def test_cipher_integer(self):

        text = 'word'
        shift = "two"
        expected = 'yqtf'
        with pytest.raises(AssertionError):
            cipher(text, shift)

    def test_cipher_upper(self):
        text = 'AND'
        shift = 2
        expected = 'CPF'
        actual = cipher(text, shift)
        assert actual == expected
        
    def test_cipher_sentence(self):
        text = 'Dogs are cute'
        shift = 2
        expected = 'Fqiu ctg ewvg'
        actual = cipher(text, shift)
        assert actual == expected