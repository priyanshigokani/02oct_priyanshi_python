#Write a Python function to check whether a number is perfect or not.

def is_per_num(n):
    sum=0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n
num = int(input("Enter a number:"))
if is_per_num(num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")