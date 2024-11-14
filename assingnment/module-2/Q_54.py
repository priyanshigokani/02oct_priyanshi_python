import random

fl=open("new.txt","r")
line=fl.read().splitlines()
print(random.choice(line))