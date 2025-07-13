#!/usr/bin/env python3

import pytest
from main import calculate

def test_addition():
    assert calculate("10", "+", "5") == 15.0

def test_subtraction():
    assert calculate("10", "-", "3") == 7.0

def test_multiplication():
    assert calculate("4", "*", "5") == 20.0

def test_division():
    assert calculate("10", "/", "2") == 5.0

def test_division_by_zero():
    result = calculate("10", "/", "0")
    assert "ゼロ除算" in result

def test_invalid_operator():
    result = calculate("10", "%", "3")
    assert "無効な演算子" in result

def test_invalid_number():
    result = calculate("abc", "+", "3")
    assert "無効な数値" in result