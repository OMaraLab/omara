"""
Unit and regression test for the omara package.
"""

# Import package, test suite, and other packages as needed
import omara
import pytest
import sys

def test_omara_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "omara" in sys.modules
