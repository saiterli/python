import builtins
import io
import os
import pytest
from app import read_csv

TEST_CSV = 'test_data.csv'

def setup_module(module):
    # Create a test CSV file
    with open(TEST_CSV, 'w') as f:
        f.write("name,age\n")
        f.write("Alice,30\n")
        f.write("Bob,25\n")

def teardown_module(module):
    # Clean up test CSV
    os.remove(TEST_CSV)

def test_read_csv_output(capsys):
    read_csv(TEST_CSV)
    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "30" in captured.out
    assert "25" in captured.out
