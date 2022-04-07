'''Here -> set: indicates that the function is going to return a set.'''
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(search4vowels('life, the universe, and everything'))
print(search4vowels('life, the universe, and everything'))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in a 'phrase'."""
    return set(letters).intersection(set(phrase))

print(search4letters('life, the universe, and everything'))
print(search4letters('life, the universe, and everything'))
print(search4letters(letters='xyx', phrase='galaxy'))
