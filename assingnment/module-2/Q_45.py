#Write a Python function to check whether a number is in a given range

def in_range(number,start,end):
    return start <= number <= end

number = 7

start = 1
end = 30
if in_range(number,start,end):
    print("Number is in the range")

else:
    print("Number is not in the range")