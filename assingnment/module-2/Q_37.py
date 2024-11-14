#Write a Python program to map two lists into a dictionary


keys = ['id','name','age']
Values = [7,'ava','25']

new_dict = {}

index =0


for key in keys:
    new_dict[key] = Values[index]
    index +=1

print(new_dict)