def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Tests
def test_add():
    assert add(2, 3) == 5
    print("Add test passed! ✅")

def test_subtract():
    assert subtract(5, 3) == 2
    print("Subtract test passed! ✅")

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All tests passed! 🎉")