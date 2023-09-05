import random
import string

#? adding the list we need to generate a password

# lower_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# upper_letter = [letter.upper() for letter in lower_letter]
# letters = lower_letter + upper_letter

numbers = ['1','2','3','4','5','6','7','8','9']
complex_character = ['#','$','%','&','*','+','-','.','>','?','@','^','_']

letters = string.ascii_uppercase + string.ascii_lowercase
complex_number = letters + str(numbers) + str(complex_character)

default_length = 12 #! default password length incase user don't enter length for they password

#? define a password generator 
def generate_password(length = default_length, is_complex = False):
    if not (12 <= length <= 18): return "error: please enter length between (12,18)", False
    password = ""
    for i in range(length):
        if is_complex:
            password += random.choice(complex_number)
        else:
            password += random.choice(letters)
    return password