#Write a Python program to write multiple strings into a file.
fl=open("WMS.txt","w")
fl.writelines("hello python \nthis is python. \npython is programming language.")
print(fl)