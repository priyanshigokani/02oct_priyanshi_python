#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple_list =[(1,4,9),(),(12,13),(7,18,30)]

tuple_list.remove(())
print(tuple_list)