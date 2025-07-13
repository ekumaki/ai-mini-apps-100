#!/usr/bin/env python3

import pytest
from main import calculate_loan_payment

def test_loan_calculation():
    result = calculate_loan_payment("1000000", "5", "10")
    assert isinstance(result, dict)
    assert result["principal"] == 1000000
    assert result["annual_rate"] == 5
    assert result["years"] == 10

def test_zero_interest():
    result = calculate_loan_payment("1200000", "0", "10")
    assert result["monthly_payment"] == 10000

def test_invalid_principal():
    result = calculate_loan_payment("0", "5", "10")
    assert "正の値" in result

def test_negative_rate():
    result = calculate_loan_payment("1000000", "-1", "10")
    assert "0以上" in result

def test_invalid_input():
    result = calculate_loan_payment("abc", "5", "10")
    assert "無効な数値" in result