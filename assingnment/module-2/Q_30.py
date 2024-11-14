#Write a Python script to concatenate following dictionaries to create a
# new one.


dict_1 = {'id':7,'name': 'ava'}
dict_2 = {'age':23,'city': 'new york'}

dict_1.update(dict_2)

print(dict_1)
