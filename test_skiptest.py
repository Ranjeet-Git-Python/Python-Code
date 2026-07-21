import sys
import pytest

pytestmark = pytest.mark.skipif(sys.platform!="win32", reason="requires windows")
const = 9/5
def cel_to_fahrenheit(const=0):
    fahrenheit = const * 9 / 5 + 32
    return fahrenheit

#print(cel_to_fahrenheit(10))
@pytest.mark.skip(reason="no reason specified")
def test_case01():
    assert type(const) == float

@pytest.mark.skipif(sys.version_info<=(3,8), reason="requires python3.14")
def test_case02():
    assert cel_to_fahrenheit() == 32

@pytest.mark.skipif(pytest.__version__ > "5.5.1", reason="pytest 5.26 requires python >= 5.26")
def test_case03():
    assert cel_to_fahrenheit(38) == 100.4