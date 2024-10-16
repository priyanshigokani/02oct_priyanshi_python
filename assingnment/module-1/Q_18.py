# Write a Python function that takes a list of words and returns the length of the longest one. 

str= "this is an apple"
words = str.split()

longest=0

for word in words:
    if len(word) > longest:
        longest = len(word)

print(f"The length of the longest word is: {longest}")