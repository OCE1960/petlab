from petlab_task.app.fizz_buzz import FizzBuzz


def app(first_input: int, second_input: int):
    try:
        fizz_buzz = FizzBuzz(first_input, second_input)
        result = fizz_buzz.process_input()
        print(f'First Input: {first_input}')
        print(f'Second Input: {second_input}')
        for index in result:
            print(index)
            
        return result
    except ValueError as e:
        print(f'Error occured: {str(e)}')
        
        raise ValueError(f'Error occured: {str(e)}') from e
        
        
if __name__ == '__main__':
    app(30, '99')