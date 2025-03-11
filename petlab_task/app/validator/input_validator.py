from petlab_task.app.validator.validator_interface import ValidatorInterface


class InputValidator(ValidatorInterface):
    """
    This is a class for validating the inputs.

    Attributes:
        first_input (int): The first supplied input.
        second_input (int): The second supplied input.
    """
    
    def __init__(self, first_input: int, second_input: int):
        self.validate(first_input = first_input, second_input = second_input)
    
    
    @staticmethod
    def _validate_is_numeric(*, first_input: int, second_input: int) ->list[int]:
        """
        Validate that provided inputs are of numeric type.

        Parameters:
            first_input (int): The first number.
            second_input (int): The second number.

        Returns:
            list: The List of validated input
        """
        try:
            first_input = int(first_input)
            second_input = int(second_input)
            return [first_input, second_input]
        except ValueError as e:
            raise ValueError('All input must be numeric') from e
    
    @staticmethod
    def validate_is_greater_or_equal_to_one(*, first_input: int, second_input: int) -> bool:
        """
        Validate that none of the provided inputs are less than one.

        Parameters:
            first_input (int): The first number.
            second_input (int): The second number.

        Returns:
            bool: if the condition is satisfied
        """
        if first_input < 1 or second_input < 1:
            raise ValueError('One of the supplied input is less than one (1)')
        
        return True
    
    @staticmethod
    def validate_is_less_than_or_egual_to_hundred(*, first_input: int, second_input: int) -> bool:
        """
        Validate that none of the provided inputs are greater than 100.

        Parameters:
            first_input (int): The first number.
            second_input (int): The second number.

        Returns:
            bool: if the condition is satisfied
        """
        if first_input > 100 or second_input > 100:
            raise ValueError('One of the supplied input is greater than hundred (100)')
        
        return True
    
    @staticmethod
    def validate(*, first_input: int, second_input: int) -> list[int]:
        """
        Validate that provided inputs are of numeric type, greater or equal to one and less than 100.

        Parameters:
            first_input (int): The first number.
            second_input (int): The second number.

        Returns:
            list: The List of validated input
        """
        try:
            
            [validated_first_input, validated_second_input] = InputValidator._validate_is_numeric(
                    first_input = first_input,
                    second_input = second_input
                )
            InputValidator.validate_is_greater_or_equal_to_one(first_input = validated_first_input, second_input = validated_second_input)
            InputValidator.validate_is_less_than_or_egual_to_hundred(first_input = validated_first_input, second_input = validated_second_input)
            
            return [validated_first_input, validated_second_input]
        except ValueError as e:
            raise e 
