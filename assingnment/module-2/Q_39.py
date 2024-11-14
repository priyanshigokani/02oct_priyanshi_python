#Write a Python program to print all unique values in a dictionary.

my_dict = {'a':6, 'b':3, 'c':7, 'd':3, 'e':7,'f':1,'g':13}

new_dict = set(my_dict.values())

print(new_dict)