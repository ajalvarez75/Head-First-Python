from flask import session

from functools import wraps

def check_logged_in(func):
    '''Call the “check_logged_in” function to determine the login status,
       then act accordingly.'''
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
