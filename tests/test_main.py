from src.main import add, sous
def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
    assert add(-10, -5) == -15
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -4.0
    print("All tests passed!")
def test_sous_functions():
    assert sous(5, 3) == 2
    assert sous(0, 0) == 0
    assert sous(-1, 1) == -2
    assert sous(1.5, 2.5) == -1.0
    assert sous(-1.5, -2.5) == 1.0
    print("All tests passed!")