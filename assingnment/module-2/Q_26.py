#Write a Python program to unzip a list of tuples into individual lists.


tuple_list = [(1,4,9),(12,13,7),(18,30,3)]

print(list(zip(*tuple_list)))
