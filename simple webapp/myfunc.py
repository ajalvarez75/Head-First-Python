
def myfunc(*args):
'''The original “myfunc” works with any list of arguments.'''
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
'''The “myfunc2” function works with any amount of key/value pairs.'''
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
'''The “myfunc3” function works with any input, whether a list of arguments, a
bunch of key/value pairs, or both.'''

'''Both “*args” and “**kwargs” appear on the “def” line.'''
    if args:
        for a in args:
            print(a, end=' ')
        print()        
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()
