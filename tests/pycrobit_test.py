"""Basic tests for pycrobit."""

import pytest

from pycrobit import Fore, Pycrobit


def test_todo(lit, capsys):
    pycrobit = Pycrobit(framerate=0.0001)
    pycrobit.display(lit)
    pycrobit.display(lit, {"*": Fore.YELLOW})
    pycrobit.wait(0.002)
    pycrobit.display(lit, {"*": Fore.GREEN})
    out, err = capsys.readouterr()
    assert not err
    assert "[33m*\x1b[" in out
    with pytest.raises(ValueError, match="asked to wait for a negative time"):
        pycrobit.wait(-1.0)
