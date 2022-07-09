import random
left = 0

list_letters = [chr(x) for x in range(ord("a"), ord("x") + 1)]
list_upper = [chr(x) for x in range(ord("A"), ord("X") + 1)]
list_lower = [chr(x) for x in range(ord("a"), ord("x") + 1)]
list_letters.extend(list_upper)
list_special = ["#", "$", "@", "&", "*", "!", "^", "%"]
list_numbers = [str(x) for x in range(10)]



# Length of pw
def gen_length():
    while True:
        try:
            length = int(input("How long do you want your password to be? : "))
            if length >= 6:
                return length
            else:
                print("Give a number above or equal to 6.")
        except ValueError:
            print("Give a number!")


# Number of letters
def num_letters():
    while True:
        try:
            letters = int(input("How many letters do you want your password to have? : "))
            return letters
        except ValueError:
            print("Give a number!")


def num_special_char():
    while True:
        try:
            special_char = int(input("How many SPECIAL letters do you want your password to have? : "))
            return special_char
        except ValueError:
            print("Give a number!")


# num of numbers in pw
def num_nums(length, letters, special_char):
    return length - letters - special_char


def gen_password(letters=0, special_char=0, num=0):
    password = []

    for i in range(num):
        password.append(random.choice(list_numbers))
    for i in range(letters):
        password.append(random.choice(list_letters))
    for i in range(special_char):
        password.append(random.choice(list_special))
    random.shuffle(password)
    return password

def check_password(password):
    lowercase = 0
    uppercase = 0
    special = 0
    number = 0
    check = 0
    for letter in password:
        # Check for lower_case letters
        if letter in list_lower:
            lowercase += 1
            continue
        # Check for upper case letters
        if letter in list_upper:
            uppercase += 1
            continue
        # Checks for numbers
        if letter in list_numbers:
            number += 1
            continue
        # Check for special characters
        if letter in list_special:
            special += 1
            continue

    if lowercase >= 1:
        check += 1

    if uppercase >= 1:
        check += 1

    if special >= 1:
        check += 1

    if number >= 1:
        check += 1

    if check == 1:
        return 1
    if check == 2:
        return 2
    if check == 3:
        return 3
    if check == 4:
        return 4


user_name = input("What is your name?")
print(f"Hello {user_name}! Let's create a password for you today, or shall you key in your own password?")
# Checks if input from user is actually "own" or "create"
user_choice = input("Please type in \"own\" or \"create\":  ")
while True:
    if user_choice.upper() == "OWN":
        break
    elif user_choice.upper() == "CREATE":
        break
    else:
        user_choice = input("Please type in \"own\" or \"create\":  ")

if user_choice.upper() == "OWN":
    user_password = input("Please key in your password so we can evaluate it: ")

    if len(user_password) < 8:
        print("Your password is weak.")

    else:
        if check_password(user_password) == 1:
            print("Your password is ok.")
        elif check_password(user_password) == 2:
            print("Your password is good.")
        elif check_password(user_password) == 3:
            print("Your password is very good.")
        elif check_password(user_password) == 4:
            print("Your password is strong!")
else:
    #Create password
    print("Let's build a password!")
    length_pw = gen_length()
    letters_pw = num_letters()
    # Check if user input a number above the length
    while letters_pw > length_pw:
        print("You're not stupid. Please don't do that.")
        letters_pw = num_letters()

    # Generate PW if there is no length left
    left = length_pw - letters_pw

    if left == 0:
        pw = gen_password(letters_pw)
        print("You do not have numbers or special characters.")
        print(*pw, sep='')

    # Continue if there is length left
    else:
        special_char = num_special_char()

        # Check that num of special characters less than the total length - the num of letters
        left = length_pw - letters_pw - special_char
        while left < 0:
            print("You're not stupid. Please don't do that.")
            special_char = num_special_char()

        # If no length left, proceed to PW GEN.
        if left == 0:
            pw = gen_password(letters_pw, special_char)
            print("You do not have numbers.")
            print(*pw, sep='')

        # Remaining length will be numbers
        else:
            num_pw = num_nums(length_pw, letters_pw, special_char)
            print(f"You will have {num_pw} number(s).")
            pw = gen_password(letters_pw, special_char, num_pw)
            print(*pw, sep='')
