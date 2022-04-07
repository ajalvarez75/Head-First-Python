def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found

print(search4vowels('casa'))

print(search4vowels('sky'))
