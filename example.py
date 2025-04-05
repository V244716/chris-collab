import pytest


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a - b  


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    assert(-459.67 < fahrenheit)
    return multiply(subtract(fahrenheit, 32), 5 / 9)


# uncomment the following test in step 5
def test_subtract():
    assert subtract(2, 3) == -1


def test_convert_fahrenheit_to_celsius():
   assert convert_fahrenheit_to_celsius(32) == 0
   assert convert_fahrenheit_to_celsius(122) == pytest.approx(50)
   with pytest.raises(AssertionError):
       convert_fahrenheit_to_celsius(-600)
