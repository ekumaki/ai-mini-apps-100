#!/usr/bin/env python3

import pytest
from main import calculate_date_diff

def test_same_date():
    result = calculate_date_diff("2023-01-01", "2023-01-01")
    assert result["total_days"] == 0

def test_one_day_diff():
    result = calculate_date_diff("2023-01-01", "2023-01-02")
    assert result["total_days"] == 1

def test_year_diff():
    result = calculate_date_diff("2022-01-01", "2023-01-01")
    assert result["total_days"] == 365

def test_order_independence():
    result1 = calculate_date_diff("2023-01-01", "2023-01-10")
    result2 = calculate_date_diff("2023-01-10", "2023-01-01")
    assert result1["total_days"] == result2["total_days"]

def test_invalid_date():
    result = calculate_date_diff("2023-13-01", "2023-01-01")
    assert "日付形式" in result