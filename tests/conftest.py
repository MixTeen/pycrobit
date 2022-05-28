import pytest


@pytest.fixture()
def off():
    return """\
.....
.....
.....
.....
....."""


@pytest.fixture()
def lit():
    return """
*****
*****
*****
*****
*****
"""


@pytest.fixture()
def diagonal():
    return """
.****
*.***
**.**
***.*
****.
"""


@pytest.fixture()
def invalid():
    return """
.***
*.***
*.**
***.*
***.
"""
