#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 


n1=int(input("enter your first number: "))
n2=int(input("enter your second number: "))
n3=int(input("enter your third number: "))

if n1==n2 or n1==n3 or n2==n3:
    sum=0

else:
    sum = n1 + n2 + n3

print("The sum is: ",sum)