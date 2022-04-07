def search4vowels(word):
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

print(search4vowels('casa'))

print(search4vowels('sky'))
