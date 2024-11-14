#write a python function that takes a list and return new list with unique elements of the first list.

def unique(list1):
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

original_list = [1,4,12,13,13,30,9,18]
print(unique(original_list))

