import pytest

from pycrobit import validate_pycrobit_str


def test_pycrobit_string():
    validate_pycrobit_str(
        """
12345
12345
12345
12345
12345
"""
    )
    with pytest.raises(ValueError, match="expected 5 characters on line n°3"):
        validate_pycrobit_str(
            """
        12345
        12345
        1234
        12345
        12345
        """
        )
