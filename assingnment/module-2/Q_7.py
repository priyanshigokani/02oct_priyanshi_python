#Write a Python function that takes two lists and returns true if they have at least one common member.


def common_num(list1,list2):
 common_num = False
 for i in list1:
   if i in list2:
     common_num = True 
     break 
 return common_num
 

list1 = [13,6,7]
list2 = [0,3,7]

result = common_num(list1,list2)
print(result)

 
   