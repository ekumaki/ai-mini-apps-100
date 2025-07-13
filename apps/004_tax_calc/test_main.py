#!/usr/bin/env python3

import pytest
from main import calculate_tax

def test_normal_tax_calculation():
    result = calculate_tax("1000", "10")
    assert result["price"] == 1000.0
    assert result["tax_rate"] == 10.0
    assert result["tax_amount"] == 100.0
    assert result["total_price"] == 1100.0

def test_zero_tax():
    result = calculate_tax("1000", "0")
    assert result["tax_amount"] == 0.0
    assert result["total_price"] == 1000.0

def test_negative_price():
    result = calculate_tax("-100", "10")
    assert "価格は0以上" in result

def test_negative_tax_rate():
    result = calculate_tax("1000", "-5")
    assert "税率は0以上" in result

def test_invalid_input():
    result = calculate_tax("abc", "10")
    assert "無効な数値" in result