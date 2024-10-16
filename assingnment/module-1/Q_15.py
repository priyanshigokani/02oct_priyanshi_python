#Write a Python program to get a single string from two given strings, separated by a space and swap the first 
# two characters of each string. 


string1 = "hello"
string2 = "python"

new_string1 = string2[0] + string1[1:]
new_string2 = string1[0] + string2[1:]

result = new_string1 + " " + new_string2

print(result)
