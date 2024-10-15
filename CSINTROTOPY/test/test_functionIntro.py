import pytest
from newTestForPrctIntro import square
from functionIntro import hello
def main():
    test_squared()#without pytest
    test_square()#with pytest
    # hello()
def test_hello():
     assert hello("Monikai") == "Hello, Monikai"
     assert hello() == "Hello, world"
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
def test_squared():
    try:
        assert square(2) == 4
        print(square(2) == 4)
    except AssertionError:
        print("Error")
    try:
        assert square(2) == 9
        print(square(3) == 9)
    except AssertionError:
        print("Error")
        print(square(2) == 9, "2 squared does not equal 9")
# def test_str():
#         main()
if __name__ == "__main__":
        main()