#Write a Python program to get unique values from a list

n=[1,4,9,13,13,7,7,30]

unique_list = []

for i in n:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)