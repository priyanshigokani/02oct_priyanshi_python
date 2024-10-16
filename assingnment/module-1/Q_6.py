#Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter: ")

if letter in 'aeiouAEIOU':
    print("The given number is vowel.")

else:
    print("The given letter is not vowel.")