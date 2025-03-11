import pytest

from petlab_task.app.fizz_buzz import FizzBuzz


class TestFizzbuzz:
    
    @pytest.mark.parametrize(
        "test_first_input, test_second_input, expected",
        [
            ("3", 8, ['fizz']),
            ("5", 8, ['buzz']),
            ("15", 8, ['fizz', 'buzz']),
            ("13", 8, []),
            ("5", 3, ['fizz', 'buzz']),
        ]
    )
    def test_fizz_is_printed_if_input_is_divisible_by_3(self, test_first_input, test_second_input, expected):
        result = FizzBuzz(test_first_input, test_second_input).process_input()
        
        assert result == expected