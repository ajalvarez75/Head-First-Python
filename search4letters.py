'''Here -> set: indicates that the function is going to return a set.'''
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(search4vowels('avion'))
print(search4vowels('sky'))

def search4letters(phrase:str, letters:str) -> set:
    """Return a set of the 'letters' found in a 'phrase'."""
    return set(letters).intersection(set(phrase))

print(search4letters('avion de la compañia americana','avion'))
print(search4letters('sky is the limit!!', 'a'))

