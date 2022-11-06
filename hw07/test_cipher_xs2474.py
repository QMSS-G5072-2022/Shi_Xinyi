from cipher_xs2474 import cipher_xs2474

import pytest

def cipher(text, shift, encrypt=True):
    
    """
    An algorithm for performing encryption or decryption which takes in original text and number of shift and returns the transformed text. 
    
    Parameters
    ----------
    text: your original text (string)
    shift: the number of shift in the alphabet that you would like to have for your text (integer)
    encrypt: transforming the text in encryption or decryption (boolean)
    
    Returns
    ----------
    The new transformed text.
    
    Examples
    ---------
    from cipher_xs2474 import cipher_xs2474
    cipher_xs2474.cipher('word, 2, encrypt = True)
    'yqtf'
    
    from cipher_xs2474 import cipher_xs2474
    cipher_xs2474.cipher('yqtf', 2, encrypt = False)
    'word'
    """
    
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