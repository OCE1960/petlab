import pytest

from petlab_task.app.validator.input_validator import InputValidator


class TestInputValidator:
    def test_all_input_must_be_numeric(self):
        with pytest.raises(ValueError) as excinfo:
            InputValidator(10, 'petlab')
            
        assert  'All input must be numeric' in str(excinfo.value)
            
    def test_any_of_the_input_must_not_be_less_than_one(self):
        with pytest.raises(ValueError)  as excinfo:
            InputValidator(10, '0')
            
        assert  'One of the supplied input is less than one (1)' in str(excinfo.value)
        
        
    def test_any_of_the_input_must_not_be_greater_than_100(self):
        with pytest.raises(ValueError)  as excinfo:
            InputValidator(101, '25')
            
        assert  'One of the supplied input is greater than hundred (100)' in str(excinfo.value)
        
    def test_all_input_are_valid(self):
        result = InputValidator.validate(first_input = 100, second_input = '1')
            
        assert 100 in result
        assert 1 in result