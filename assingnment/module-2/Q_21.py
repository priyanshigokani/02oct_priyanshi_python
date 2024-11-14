#Write a Python program to convert a list to a tuple.

user_list=[]
list=int(input("Enter your number of element: "))


for i in range(list):
    name=(input("Enter your element name: "))
    user_list.append(name)

print(tuple(user_list))