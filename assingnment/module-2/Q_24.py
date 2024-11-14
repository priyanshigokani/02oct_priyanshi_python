#Write a Python program to find the repeated items of a tuple.

my_tuple = (1,4,9,7,13,12,18,13,30,7)

for i in range(0,len(my_tuple)):
    for j in range(i+1,len(my_tuple)):
        if my_tuple[i] == my_tuple[j]:
            print("Repeated items is: ", my_tuple[i])
    
    