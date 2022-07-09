# Create a password for user
import random


# Length of pw, needs to be more than or equal to 8
def gen_length():
    while True:
        try:
            length = int(input("How long do you want your password to be? : "))
            if length >= 8:
                return length
            else:
                print("Give a number above or equal to 8.")
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


# num of numbers in pw
def num_nums(length, letters):
    return length - letters


def gen_password(num, letters):
    password = []
    list_letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    list_letters.extend([chr(x) for x in range(ord('a'), ord('z') + 1)])
    list_num = list(range(10))
    for i in range(num):
        password.append(random.choice(list_num))
    for i in range(letters):
        password.append(random.choice(list_letters))

    random.shuffle(password)
    return password


print("Let's build a password!")
length_pw = gen_length()
letters_pw = num_letters()
num_pw = num_nums(length_pw, letters_pw)
print(f"You will have {num_pw} numbers.")
pw = gen_password(num_pw, letters_pw)
print(*pw,sep='')