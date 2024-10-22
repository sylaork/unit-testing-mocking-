#test doubles are objects that are used in unit tests as replacements to the real production system collaborators
#Replacing the actual dependencies of a method or class with fake versions.
'''
* unittest.mock * mock class example
#example
def test_Foo():
   bar=Mock()
   functionThatUsesBar(bar)
   bar.assert_called_once(

* monkeypatch example *

def callIt():
  print('Hello World')

def test_patch(monkeypatch):
   monkeypatch(callIt, Mock())
   callIt()
   callIt.assert_called_once()

'''

import pytest
from unittest.mock import MagicMock
from LineReader import readFromFile
from pytest import raises
'''
def test_canCallReadFromFile():
    readFromFile('blah')

'''
@pytest.fixture() #fixed baseline so the tests go reliably
def mock_open(monkeypatch): #monkey patching is a technique used to dynamically update the behavior of a piece of code at run-time
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line') #return_value parameter specifies the return value when the Mock is called
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open) #monkeypatch.setattr to patch the function or property with your desired testing behavior
    return mock_open

#In the test case we want the functon
# to actually do the work of opening a file, reading a line and returning it
#we don't wanna actually have to open a file for this test because it's slows the test down
#Instead we mock out the open function to return a MagicMock object and we'll add a line read attribute to the mock
#which is also a MagicMock object that'll return the test string was returned

def test_returnsCorrectsString(mock_open, monkeypatch):
    #pytest provides the monkeypatch test fixture to allow a test
    #to dynamically replace: module and class attributes, dictionary entries
    #environment variables
    mock_file=MagicMock()
    mock_file.readline=MagicMock(return_value='test line')
    mock_open=MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)
    result=readFromFile('blah')
    mock_open.assert_called_once_with('blah', 'r')
    assert result=='test line'

def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists=MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with raises(Exception):
        result=readFromFile('blah')

'''
What is Mocking?
Replacing the actual dependencies of a method or class with fake versions.
These fake versions can be controlled independently.

It is useful in the following cases:
When there is no need for a real database or web service.
The real object is when you want to protect yourself from unexpected errors.
Example: A method that pulls data from a database. However, it is not desired to use a real database every time, because this can be slow. Instead, a database mock is created.

When should mocking be used more?
When the code depends too much on external systems.
Example: Web services or databases. For example, if you had to call a real web service every time, this

Would be slow and difficult to test.

When should mocking be used less?
When the entire system needs to be tested in integration tests, including the real database or real web service.
Example: When you want to make sure everything works properly together and the class doesn't have complex dependencies.
For example: A method that sums 2 random numbers does not need a mock.
'''
