import pytest

from petlab_task.app.fizz_buzz import FizzBuzz
from petlab_task.app.main import app


@pytest.mark.parametrize(
    "test_first_input, test_second_input, expected",
    [
        ("30", 9, ['fizz', 'fizz', 'buzz']),
        ("14", 8, []),
    ]
)
def test_app(test_first_input, test_second_input, expected):
    result = app(test_first_input, test_second_input)
    
    assert result == expected
    
def test_app_throws_exception_if_any_of_the_input_is_not_numeric():
        with pytest.raises(ValueError)  as excinfo:
            app(30, 'ert')
            
        assert  'Error occured: All input must be numeric' in str(excinfo.value)
        
def test_app_throws_exception_if_any_of_the_input_is_less_than_1():
        with pytest.raises(ValueError)  as excinfo:
            app(30, '0')
            
        assert  'Error occured: One of the supplied input is less than one (1)' in str(excinfo.value)
        
def test_app_throws_exception_if_any_of_the_input_is_greater_than_100():
        with pytest.raises(ValueError)  as excinfo:
            app(30, '102')
            
        assert  'Error occured: One of the supplied input is greater than hundred (100)' in str(excinfo.value)