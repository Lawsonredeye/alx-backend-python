## Python UNITTEST MOCK

python mock is a very crucial way of testing your codes to see how it handles not only functionality but how every part of the program works as a whole.

It uses the Mock class from the unittest library to check the code that is to be run.

It has methods which can be used to check how a function was called, executed and also operates in terms of overall functioning.

It uses several methods like:
- .assert_called() - checks if a specific method of a class was called
- .assert_called_once() - checks how many times the method was called
- .assert_called_with(*args, **kwargs) - compares the param passed on the keyword with the original keyword
- .assert_called_once_with(*args, **kwargs) - check if the keyword passed to a method was called more than once.

If any of these assertion fails the assert raises an AssertionError with details on the error raised else it doesn't return any error.

The .side_effect is also useful to dictate what happens to functions that has a specific return value that is unknown or that might change.
