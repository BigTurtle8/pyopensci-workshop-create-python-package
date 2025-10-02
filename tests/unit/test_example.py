"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_bigturtle8.example import *

def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_sub_numbers():
    """
    Test that sub_numbers works as expected.
    """
    out = sub_numbers(1, 2)
    expected_out = -1
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_mul_numbers():
    """
    Test that mul_numbers works as expected.
    """
    out = mul_numbers(1, 2)
    expected_out = 2
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_div_numbers():
    """
    Test that div_numbers works as expected.
    """
    out = div_numbers(1, 2)
    expected_out = 0.5
    assert  out == expected_out, f"Expected {expected_out} but got {out}"