import pytest
import sys
from io import StringIO
from contextlib import redirect_stdout
from solution import main

# Helper function to capture the output of the function
def run_test_case(input_str):
    input_data = StringIO(input_str)
    output_data = StringIO()
    
    sys.stdin = input_data
    with redirect_stdout(output_data):
        main()
    
    sys.stdin = sys.__stdin__  # Reset stdin back to original
    return output_data.getvalue().strip()

def test_basic_case():
    input_data = """2
3
5 -3 2
4
-10 -5 1 4"""
    expected_output = "29\n17"
    assert run_test_case(input_data) == expected_output

def test_all_positive_numbers():
    input_data = """1
5
1 2 3 4 5"""
    expected_output = "55"
    assert run_test_case(input_data) == expected_output

def test_all_negative_numbers():
    input_data = """1
4
-7 -5 -3 -2"""
    expected_output = "0"
    assert run_test_case(input_data) == expected_output

def test_mixed_positive_and_zero():
    input_data = """1
6
0 3 7 0 -2 8"""
    expected_output = "122"
    assert run_test_case(input_data) == expected_output

def test_edge_case_x_is_1():
    input_data = """2
1
-99
1
100"""
    expected_output = "0\n10000"
    assert run_test_case(input_data) == expected_output

def test_maximum_values():
    input_data = """1
100
100 99 -98 -97 -96 95 94 93 -92 -91 90 89 88 -87 -86 85 84 83 -82 -81 80 79 78 -77 -76 75 74 73 -72 -71 70 69 68 -67 -66 65 64 63 -62 -61 60 59 58 -57 -56 55 54 53 -52 -51 50 49 48 -47 -46 45 44 43 -42 -41 40 39 38 -37 -36 35 34 33 -32 -31 30 29 28 -27 -26 25 24 23 -22 -21 20 19 18 -17 -16 15 14 13 -12 -11 10 9 8 -7 -6 5 4 3 -2 -1 0"""
    expected_output = "199446"
    assert run_test_case(input_data) == expected_output

def test_edge_case_x_is_100_with_zeros_and_negatives():
    input_data = """1
100
-1 0 -2 0 -3 0 -4 0 -5 0 -6 0 -7 0 -8 0 -9 0 -10 0 -11 0 -12 0 -13 0 -14 0 -15 0 -16 0 -17 0 -18 0 -19 0 -20 0 -21 0 -22 0 -23 0 -24 0 -25 0 -26 0 -27 0 -28 0 -29 0 -30 0 -31 0 -32 0 -33 0 -34 0 -35 0 -36 0 -37 0 -38 0 -39 0 -40 0 -41 0 -42 0 -43 0 -44 0 -45 0 -46 0 -47 0 -48 0 -49 0 -50 0"""
    expected_output = "0"
    assert run_test_case(input_data) == expected_output

def test_provided_example():
    input_data = """2
4
3 -1 1 14
5
9 6 -53 32 16
"""
    expected_output = "206\n1397"
    assert run_test_case(input_data) == expected_output