"""
unittesting or pytest
"""
import pytest 
import secure_otp

def test_correct_otp():
    assert secure_otp(int=4) == True

def test_wrong_otp():
    assert secure_otp(4<int>4) == False