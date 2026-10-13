
from calculator import add, subtract


# test addition with positive numbers
def test_add():
    assert add(2, 3) == 5


# test subtraction with positive numbers
def test_subtract():
    assert subtract(5, 3) == 2


# test subtraction with negative numbers
def test_subtract_negative():
    assert subtract(-5, -3) == -2


# test subtraction with zero
def test_subtract_zero():
    assert subtract(5, 0) == 5
























with open("file.txt", "r") as file:
    content = file.read()

print(content)