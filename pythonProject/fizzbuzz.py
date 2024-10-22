import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value,5):
            return 'FizzBuzz'
        return 'Fizz'

    elif value + 0.0 != value:
        return 'Value should be int'

    elif value<0:
        return 'Value cannot be negative'


    elif isMultiple(value, 5):
        return 'Buzz'
    return str(value)


def isMultiple(value, mod):
    return (value % mod)==0

def checkFizzBuzz(value, expectedRate): #mocking
    rate=fizzBuzz(value)
    assert rate==expectedRate


def test_returns1With1PassedIn():
    checkFizzBuzz(1, '1')

def test_returns2With2PassedIn():
    checkFizzBuzz(2, '2')

def test_returnsFizzWith3PassedIn(): #3 == FIZZ
    checkFizzBuzz(3, 'Fizz')

def test_returns4With4PassedIn():
    checkFizzBuzz(4, '4')

def test_returnsBuzzWith5PassedIn(): # 5==BUZZ
    checkFizzBuzz(5, 'Buzz')

def test_returns6With6PassedIn():
    checkFizzBuzz(6, 'Fizz')

def test_returnsBuzzWith10PassedIn(): #multiple of 5 so buzz
    checkFizzBuzz(10, 'Buzz')

def test_returnsFizzBuzzWith15PassedIn(): #multiple of both 3 and 5
    checkFizzBuzz(15, 'FizzBuzz')

def test_negativeNbrReturnsOutput(): #invalid for negatives
    checkFizzBuzz(-1, 'Value cannot be negative')

def test_returnsInvalidTypeStringInput(): #invalid for string
    try:
        fizzBuzz('string')
    except TypeError:
        assert True
    else:
        assert False

def test_returnsInvalidTypeFloatInput(): #invalid for float
    try:
        fizzBuzz('4.5')
    except TypeError:
        assert True
    else:
        assert False