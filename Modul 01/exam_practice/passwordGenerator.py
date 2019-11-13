import string
import random

def passwordGenerator(param):
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(char) for i in range(param))

userInput = int(input('How many characters do you want?: '))
print(passwordGenerator(userInput))