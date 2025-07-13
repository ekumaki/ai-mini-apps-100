#!/usr/bin/env python3

import pytest
from main import calculate_roi

def test_positive_roi():
    result = calculate_roi("1000", "1200")
    assert result["roi_percent"] == 20.0
    assert result["gain_loss"] == 200

def test_negative_roi():
    result = calculate_roi("1000", "800")
    assert result["roi_percent"] == -20.0
    assert result["gain_loss"] == -200

def test_with_period():
    result = calculate_roi("1000", "1200", "2")
    assert result["period_years"] == 2
    assert 9 < result["annual_return"] < 10  # 約9.54%

def test_zero_investment():
    result = calculate_roi("0", "1000")
    assert "正の値" in result

def test_invalid_period():
    result = calculate_roi("1000", "1200", "0")
    assert "period_error" in result