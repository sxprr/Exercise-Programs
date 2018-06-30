# This is my first programming exercise, a password generator
# This is what my approach was to programming.

# take a look and give me feedback.

import os 
import random 
import string

UserPswrdLvl = input("Choose password strength by corresponding letter - [Short (S)]-[Medium (M)]-[Long (L)]")
UserAlphNum = input("Alphanumeric? (Y/N)?")

# function to generate small password string

def PassWordGen_S():
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)

    return 0 

# function to generate medium password string
def PassWordGen_M():
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)

    
    return 0 

# function to generate medium password string
def PasswordGen_L():
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)
    random.choice(string.ascii_letters)

    return 0 

print(PassWordGen_S)
print(PassWordGen_M)
print(PasswordGen_L)

