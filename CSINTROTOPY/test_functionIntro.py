import pytest
from functionIntro import squared

def main():
    test_squared()#without pytest
    test_square()#with pytest
def test_square():
    assert squared(2) == 4
    assert squared(3) == 9
    assert squared(-2) == 4
    assert squared(-3) == 9
    assert squared(0) == 0
def test_squared():
    try:
        assert squared(2) == 4
        print(squared(2) == 4)
    except AssertionError:
        print("Error")
    try:
        assert squared(2) == 9
        print(squared(3) == 9)
    except AssertionError:
        print("Error")
        print(squared(2) == 9, "2 squared does not equal 9")
# def test_str():
#         main()
if __name__ == "__main__":
        main()