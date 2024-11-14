#write a Python program to check whether a list contains a sub list

my_list =['mango','watermelon','strawberry',[1,3,7],'kiwi']
sub_list = [1,3,7]

if sub_list in my_list:
    print("Yes")

else:
    print("No")
