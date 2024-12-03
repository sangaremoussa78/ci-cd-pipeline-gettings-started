from src.main import add
def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
    assert add(-10, -5) == -15
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -4.0
    print("All tests passed!")