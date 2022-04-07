tasks = open('todos.txt')

for chore in tasks:
    print(chore, end='')

tasks.close()

"""
'r' Open a file for reading. This is the default mode and, as such, is optional. When no second argument is
provided, 'r' is assumed. It is also assumed that the file being read from already exists.
'w' Open a file for writing. If the file already contains data, empty the file of its data before continuing.
'a' Open a file for appending. Preserve the file’s contents, adding any new data to the end of the file (compare
this behavior to 'w').
'x' Open a new file for writing. Fail if the file already exists (compare this behavior to 'w' and to 'a').
"""
