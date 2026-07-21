
class TestClass():
    def test_type(self):
       assert type(1) == int
       assert type(1.0) == float

    def test_strs(self):
       assert str.upper("python") == "PYTHON"
       assert str.lower("Python") == "python"