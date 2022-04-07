'''Here -> set: indicates that the function is going to return a set.'''
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(search4vowels('avion'))
print(search4vowels('sky'))

