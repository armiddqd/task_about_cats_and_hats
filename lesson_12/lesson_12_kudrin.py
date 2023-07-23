# Task 1 - Write a decorator that ensures a function is
# only called by users with a specific role


def is_admin(func):
    def wrapper(**kwargs):
        if kwargs['user_type'] != 'admin':
            raise ValueError('Permission denied')
        else:
            return func(user_type=kwargs['user_type'])
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print('Prepare to a mindblowing thing')
    print('If you will add 2 to 3 it will be:')
    print(2+3)
    print('Wow it\'s true!')
    print('Imagine what secrets are hidden from regular people!')
    print('That\'s crazy. I can\'t believe...')


show_customer_receipt(user_type='user')
# > ValueError: Permission denied


show_customer_receipt(user_type='admin')
# > function pass as it should be


# Task 2 - Write a decorator that wraps a function
# in a try-except block


def catch_errors(func):
    def wrapper(data):
        try:
            return func(data)
        except Exception as error:
            # didn't find a method how to make example's text
            # so decided to handle error just by mask mapping
            # Will fix if needed
            print(f'Found 1 error during execution of \
                  your function: {type(error).__name__} {str(error)}')

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
# Found 1 error during execution of your function: KeyError no such key as foo

some_function_with_risky_operation({'key': 'bar'})
# bar
