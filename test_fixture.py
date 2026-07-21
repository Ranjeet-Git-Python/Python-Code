import pytest

@pytest.fixture()
def setup_list():
    print("\nsetup_list\n")
    city = ["Pune","Bangalore","Patna", "Delhi","Mumbai"]
    return city

def test_getitem(setup_list):
    print(setup_list[0:3])
    assert setup_list[0] == "Pune"
    assert setup_list[::2] == ["Pune","Patna","Mumbai"]