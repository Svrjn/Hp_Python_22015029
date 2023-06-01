#this program test for upper and lower case
x = input("Enter a letter: ")
if ord(x) >= 65 and ord(x) <= 90:
    print(x, "is an uppercase")
elif ord(x) >= 97 and ord(x) <= 122:
    print(x, "is lowercase")
else:
    print(x, "is not a letter.")
