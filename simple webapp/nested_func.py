
def outer():
    def inner():
       print('This is inner.')
       '''The “inner” function is defined within the enclosing function’s
        suite.'''

    print('This is outer, invoking inner.')
    inner()
'''The printed messages appear in the order: “outer” first, then “inner”.'''
