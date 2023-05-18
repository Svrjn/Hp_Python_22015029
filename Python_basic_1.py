#program to display name,age and phone number
name=input("what is your name\t")
age=int(input("how old are you?\t"))
#your age should be only in numeric form,e.g 10
phone=int(input("Enter your phone number\t"))
print("Hello {}, you are {} years old with the phone number ({})".format(name,age,phone))
