#Write a Python program to remove duplicates from a list.

my_list=[1,2,3,6,7,9,1,3]
new_list=[]

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print("new list: ",new_list)