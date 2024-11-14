#Write a Python function to get the largest number, smallest num and sum of all from a list

def list_of_numbers(n):
    largest=n[0]
    smallest=n[0]
    total = 0

    for num in n:
        if num > largest :
            largest = num
        if num < smallest:
            smallest = num
        total += num

    return largest , smallest,total
    
n = [7,1,0,3,13,6]
largest,smallest,total=list_of_numbers(n)
print("largest: ",largest)
print("smallest: ",smallest)
print("total: ",total)

