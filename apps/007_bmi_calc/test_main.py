#!/usr/bin/env python3

import pytest
from main import calculate_bmi

def test_normal_bmi():
    result = calculate_bmi("170", "65")
    assert 20 <= result["bmi"] <= 25
    assert result["category"] == "普通体重"

def test_underweight():
    result = calculate_bmi("170", "50")
    assert result["bmi"] < 18.5
    assert result["category"] == "低体重"

def test_overweight():
    result = calculate_bmi("170", "80")
    assert result["bmi"] >= 25
    assert "肥満" in result["category"]

def test_invalid_values():
    result = calculate_bmi("0", "65")
    assert "正の値" in result

def test_invalid_input():
    result = calculate_bmi("abc", "65")
    assert "無効な数値" in result