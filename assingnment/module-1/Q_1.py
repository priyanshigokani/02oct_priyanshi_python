# Write a Python program to check if a number is positive, negative or zero.


number = int(input("Enter your number: "))

if number < 0:
    print("The number is negative.")

elif number > 0 :
    print("The number is positive.")

else:
    print("The number is zero")