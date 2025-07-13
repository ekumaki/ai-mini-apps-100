#!/usr/bin/env python3

import pytest
import math
from main import calculate_advanced

def test_power():
    assert calculate_advanced("2 ^ 3") == 8.0

def test_sqrt():
    assert calculate_advanced("sqrt 16") == 4.0

def test_sqrt_negative():
    result = calculate_advanced("sqrt -4")
    assert "負の数" in result

def test_percent():
    assert calculate_advanced("20 percent 50") == 10.0

def test_log():
    assert abs(calculate_advanced("log 100") - 2.0) < 0.0001

def test_sin():
    assert abs(calculate_advanced("sin 90") - 1.0) < 0.0001

def test_modulo():
    assert calculate_advanced("10 % 3") == 1.0