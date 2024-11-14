#Write a Python program to generate and print a list of first and last 5 elements here the values are square of
#s numbers between 1 and 30.

sqr=[i ** 2 for i in range(1,31)]

f_five = sqr[:5]

l_five = sqr[-5:]

print("First 5 numbers: ",f_five)
print("Last 5 numbers: ",l_five)
