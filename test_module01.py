
def test_t1():
    assert 5+5==10
    assert 5*5==25
    assert True
def test_t2():
    assert 5+5==10, "instantly fail"

def test_t3():
    assert 5//2==2