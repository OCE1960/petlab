from petlab_task.app.validator.validator_interface import ValidatorInterface


class InputValidator(ValidatorInterface):
    
    def __init__(self, first_input: int, second_input: int):
        self.validate(first_input = first_input, second_input = second_input)
        
    @staticmethod
    def _validate_is_numeric(*, first_input: int, second_input: int) ->list[int]:
        try:
            first_input = int(first_input)
            second_input = int(second_input)
            return [first_input, second_input]
        except ValueError as e:
            raise ValueError('All input must be numeric') from e
    
    @staticmethod
    def _validate_is_greater_or_equal_to_one(*, first_input: int, second_input: int) -> bool:
        if first_input < 1 or second_input < 1:
            raise ValueError('One of the supplied input is less than one (1)')
        
        return True
    
    @staticmethod
    def _validate_is_less_than_or_egual_to_hundred(*, first_input: int, second_input: int) -> bool:
        if first_input > 100 or second_input > 100:
            raise ValueError('One of the supplied input is greater than hundred (100)')
        
        return True
    
    @staticmethod
    def validate(*, first_input: int, second_input: int) -> list[int]:
        [validated_first_input, validated_second_input] = InputValidator._validate_is_numeric(first_input = first_input, second_input = second_input)
        InputValidator._validate_is_greater_or_equal_to_one(first_input = validated_first_input, second_input = validated_second_input)
        InputValidator._validate_is_less_than_or_egual_to_hundred(first_input = validated_first_input, second_input = validated_second_input)
        
        return [validated_first_input, validated_second_input] 
