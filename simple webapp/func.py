'''The “apply” function accepts a function object as an argument.
The “object” annotation helps to confirm our intention here(and the use of
the argument name “func” is a common convention).'''

def apply(func: object, value: object) -> object:
    '''Any value (of any type) can be passed as the second argument. Again, the
    annotations hint at what’s allowed as an argument type here: any object.'''
    return func(value)
'''The function (passed as an argument) is invoked, with the “value” passed
to it as its only argument. The result of this function call is returned
from the “apply” function.'''

