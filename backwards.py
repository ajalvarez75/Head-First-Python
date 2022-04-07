book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
backwards = booklist[::-1]
''.join(backwards)
#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.
print(backwards)