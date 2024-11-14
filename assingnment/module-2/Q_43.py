#Write a Python program to create a dictionary from a string.


string1 = "hello python"

char_count = {}

for i in string1:
    if i in char_count:
        char_count[i] += 1
    
    else:
        char_count[i] = 1

print(char_count)