import pytest
from main import *

def test_is_limit_five():
    operations = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    expected_result = True
    assert is_limit_five(operations) == expected_result

def test_is_valid_operator():
    operator_1 = "32 + 698"
    operator_2 = "3801 - 2"
    
    assert is_valid_operator(operator_1) == True
    assert is_valid_operator(operator_2) == True


def  test_is_valid_digit():
    digit_1 = "2023"
    digit_2 = "102023"

    assert  is_valid_digit(digit_1) == True
    assert  is_valid_digit(digit_2) == False

def test_sum():
    operand_1 = "32"
    operand_2 = "8"

    assert sum_ar(operand_1, operand_2) == 40

def test_sustrac():
    operand_1 = "32"
    operand_2 = "8"

    assert sustrac(operand_1, operand_2) == 24

def test_max_lenght_str():
    operation = ["32", "+", "8"]
    assert max_lenght_str(operation) == 2


