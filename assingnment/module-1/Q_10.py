#Write a Python program to get the Factorial number of given number. 

n = int(input("Enter your number: "))

factorial=1

if n < 0:
    print("Wring input!")

else:
    for i in range(1,n+1):
        factorial = factorial*i
        print("the factorial is :", factorial)