#Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a':1, 'b':4, 'c':9, 'd':12, 'e':13,'f':18,'g':30}

my_list = []

for i in my_dict.values():
    my_list.append(i)

my_list.sort()

print("Highest value: ", my_list[-1])
print("Second Highest value: ", my_list[-2])
print("Third Highest value: ", my_list[-3])