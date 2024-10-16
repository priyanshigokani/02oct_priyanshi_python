#Write a Python function to reverses a string if its length is a multiple of 4.


str = "hello"

if len(str) % 4 ==0:
    result=str[::-1]

else:
    result = str

print(result)