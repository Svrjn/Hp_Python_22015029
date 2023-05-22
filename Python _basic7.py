#progam that print numbers from 1 to 50

# any number divisible by 3 prints boy

#any number divisible by 5 prints girl

#any number that is divisible by both 3 and 5 prints couple

for num in range(1, 51):

    if num % 3 == 0 and num % 5 == 0:

        print("Couple,")

    elif num % 3 == 0:

        print("Boy,")

    elif num % 5 == 0:

        print("Girl,")

    else:

        print(num,end=",")
