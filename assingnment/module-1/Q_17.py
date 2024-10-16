''' Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. '''

str = "This person is not poor "

not_index =str.find('not')
poor_index = str.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
    result = str[:not_index] + 'good' + str[poor_index + 4:]

else:
    result = str

print(result)