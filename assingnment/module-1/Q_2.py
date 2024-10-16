#Write a Python program to get the Factorial number of given number.  
num = int(input("Enter your number: "))
n1=0
n2=1

for i in range(num):
    print(n1, end=" ")

    n1, n2 = n2, n1 + n2