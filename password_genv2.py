# Create a password for user
import random
left = 0

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
    list_letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    list_lower = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    list_letters.extend(list_lower)
    list_num = list(range(10))
    special_character_list = ['#', '@', '$', '%', '*', '!']

    for i in range(num):
        password.append(random.choice(list_num))
    for i in range(letters):
        password.append(random.choice(list_letters))
    for i in range(special_char):
        password.append(random.choice(special_character_list))
    random.shuffle(password)
    return password


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
        print(f"You will have {num_pw} number/numbers.")
        pw = gen_password(letters_pw, special_char, num_pw)
        print(*pw, sep='')

