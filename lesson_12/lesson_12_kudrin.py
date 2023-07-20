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
    # Some very dangerous operation
    print('weeee')


show_customer_receipt(user_type='user')
# > ValueError: Permission denied


show_customer_receipt(user_type='admin')
# > function pass as it should be
