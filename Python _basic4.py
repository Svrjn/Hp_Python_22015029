#program to determine leap year
year=int(input("Enter year to be checked:\t"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("{} is a leap year.".format(year))
else:
    print("{} is a lunar year.".format(year))







