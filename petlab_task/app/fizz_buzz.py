from petlab_task.app.validator.input_validator import InputValidator


class FizzBuzz:
    """
    This is a class for checking if the inputs are either divisible by three or five.

    Attributes:
        first_input (int): The first supplied input.
        second_input (int): The second supplied input.
    """
    def __init__(self, first_input: int, second_input: int):
        self.result = []
        [self.first_input, self.second_input] = InputValidator.validate(first_input = first_input, second_input = second_input)
        
    
    def __str__(self):
        return f'First Input: {self.first_input}, Second Input: {self.second_input}'
      
    def process_input(self) -> list[int]:
        self.is_number_divisible_by_three()
        self.is_number_divisible_by_five()
        
        return self.result
    
    def is_number_divisible_by_three(self) -> None:
        """
        This method checks if any of the input is divisble by 3 and update the result with fizz.
        """
        if self.first_input % 3 == 0:
            self.result.append('fizz')
            
        if self.second_input % 3 == 0:
            self.result.append('fizz')
    
    def is_number_divisible_by_five(self) -> None:
        """
        This method checks if any of the input is divisble by 5 and update the result with buzz.
        """
        if self.first_input % 5 == 0:
            self.result.append('buzz')
            
        if self.second_input % 5 == 0:
            self.result.append('buzz')
        