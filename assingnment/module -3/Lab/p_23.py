#Write a Python program to search for a word in a string using re.search().
import re
my_str="hello python!"
x=re.search('Python',my_str)
print(x)
if x:
    print("Match done!")
else:
    print("Error!")