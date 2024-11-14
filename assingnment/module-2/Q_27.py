#Write a Python program to convert a list of tuples into a dictionary.


user_list=[]
list=int(input("Enter your number of element: "))


for i in range(list):
    key =(input("Enter your key name:  "))
    value = input("Enter your value : ")
    user_list.append((key ,value))

result_dict=dict(user_list)

print(result_dict)