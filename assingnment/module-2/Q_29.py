# Write a Python script to sort (ascending and descending) a dictionary by value.


import operator
my_dict = {"a":1,"b":30,"c":13,"d":18,"e":12,"f":4,"g":9}

x=sorted(my_dict.items(),key=operator.itemgetter(1))
print(x)

y=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
print(y)


