import json
import re
import random
def save_user_data(users):
    with open("users_data.json", "w") as file:
        json.dump(users, file)


def sign_up():
    print("=====Welcome To  Saviour Computers=====")
    captcha1 = random.randint(0,10)
    captcha2 = random.randint(0,10)
    pattern = r"^(?=.*[A-Z])[a-zA-Z]{4,8}$"
    name_pattern = r'^([A-Za-z]+)\s+([A-Za-z]+)\s+([A-Za-z]+)$'
    user_name_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    
    try:
        with open("users_data.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    while True:
        name = input("Enter your name ")
        if re.match(name_pattern, name):
            break
        print("Invallid name input, enter your three names")
    
    while True:
        username = input("Enter a username: ")
        if username in users:
            
            print("Username already exists. Please try again.")
            continue
        elif re.match(user_name_pattern, username):
            break
        print("invalid username pattern, note: no space")

      
        
            
    while True:
        password = input("Enter a password (4-8 characters, at least one uppercase): ")
        if re.match(pattern, password):
            break
        print("Invalid password pattern. Please try again.")

    while True:
        try:
            answer = int(input(f"Please solve the CAPTCHA: {captcha1} + {captcha2} = "))
            if answer == captcha1 + captcha2:
                break
            print("Incorrect CAPTCHA. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    users[username] = password

    save_user_data(users)
    print(" You have successful sign up with saviour computers.\n Please use sign in option to access your account\n.")
    print(f'your name is {name}\n username is {username}\n Password is {password}')

def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load existing user data from JSON file
    user_data = load_user_data()

    # Check if username exists and password matches
    if username in user_data and user_data[username] == password:
        print("Sign in successful!")
    else:
        print("Invalid username or password. Please try again.")

def retrieve_password():
    username = input("Enter your username: ")

    # Load existing user data from JSON file
    user_data = load_user_data()

    # Check if username exists
    if username in user_data:
        print("Your password is:", user_data[username])
    else:
        print("Username not found.")

def load_user_data():
    try:
        with open('users_data.json') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

def save_user_data(user_data):
    with open('users_data.json', 'w') as file:
        json.dump(user_data, file)

# Main program
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Retrieve Password")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    elif choice == '3':
        retrieve_password()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
