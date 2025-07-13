#!/usr/bin/env python3

import pytest
from main import calculate_age

def test_age_calculation():
    result = calculate_age("1990-01-01", "2023-01-01")
    assert result["age_years"] == 33

def test_birthday_not_yet():
    result = calculate_age("1990-06-15", "2023-03-01")
    assert result["age_years"] == 32

def test_birthday_passed():
    result = calculate_age("1990-01-15", "2023-03-01")
    assert result["age_years"] == 33

def test_invalid_date_format():
    result = calculate_age("1990/01/01")
    assert "日付形式" in result

def test_total_days():
    result = calculate_age("2020-01-01", "2020-01-02")
    assert result["total_days"] == 1