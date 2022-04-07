
def outer():
    def inner():
    '''The “inner” function is still defined within “outer”.'''
       print('This is inner.')

    print('This is outer, returning inner.')
    return inner
    '''The “return” statement does not invoke “inner”; instead, it returns
    the “inner” function object to the calling code.'''
