import pytest
pytestmark = [pytest.mark.smoke,pytest.mark.strtest]

const = 9/5
def cel_to_fahrenheit(const = 0):
    fahrenheit = const * 9 / 5 + 32
    return fahrenheit

def test_t1():
    assert 5+5==10
    assert 5*5==25
    assert True

@pytest.mark.sanity
def test_t2():
    assert 5+5==10, "internally fail"

def test_t3():
    assert 5//2==2

@pytest.mark.sanity
@pytest.mark.skip(reason="no reason specified")
def test_case01():
    assert type(const) == float

@pytest.mark.sanity
def test_case02():
    assert cel_to_fahrenheit() == 32

@pytest.mark.sanity
@pytest.mark.str
def test_case03():
    assert cel_to_fahrenheit(38) == 100.4