# Write a Python function to insert a string in the middle of a string. 

str1= "hello world"

str2= " welcome to"

middle_index= len(str1) //2

result= str1[:middle_index] + str2 + str1[middle_index:]

print(result)


