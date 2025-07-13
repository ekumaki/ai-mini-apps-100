#!/usr/bin/env python3

import pytest
from main import convert_interest_rate

def test_daily_to_annual():
    result = convert_interest_rate("0.01", "日", "年")
    assert isinstance(result, dict)
    assert result["annual_rate"] > 3  # 複利効果で3%超

def test_monthly_to_annual():
    result = convert_interest_rate("1", "月", "年")
    assert isinstance(result, dict)
    assert 12 < result["annual_rate"] < 13  # 約12.68%

def test_same_period():
    result = convert_interest_rate("5", "年", "年")
    assert abs(result["converted_rate"] - 5) < 0.001

def test_invalid_period():
    result = convert_interest_rate("5", "時間", "年")
    assert "無効な期間" in result

def test_negative_rate():
    result = convert_interest_rate("-1", "月", "年")
    assert "0以上" in result