import pytest

from pycrobit import Fore, validate_color_map


def test_colormap():
    with pytest.raises(ValueError, match="color '1' for 'x'"):
        validate_color_map({"x": 1})
    validate_color_map({"x": Fore.RED})
