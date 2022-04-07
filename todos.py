todos = open('todos.txt', 'a')

print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

todos.close()
#As we have nothing else to add to our to-do list, let’s close the file by
#calling the close method, which is made available by the interpreter to
#every file stream:
