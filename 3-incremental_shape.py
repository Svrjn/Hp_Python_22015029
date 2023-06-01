#Program for # increment
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Only integer character is allowed, try again")
        continue
    break

for i in range(num):
    print("#"*(i+1))