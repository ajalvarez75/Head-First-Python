vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:

    if letter in vowels:

        found[letter] +=1
'''K stand for key and v for value'''            
for k, v in sorted(found.items()):
    print(k,'was found', v, 'time(s).')
