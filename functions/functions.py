import string
import secrets

password = []
symbols = list(string.punctuation)
numbers = list(string.digits)
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)


def create_password(length, s, n, lowerChar, upperChar):
    options = []
    password = []
    counter = 0
    checkCounter = s + n + lowerChar + upperChar
    if checkCounter > 0:
        if s == 1:
            options.append(symbols)
        if n == 1:
            options.append(numbers)
        if lowerChar == 1:
            options.append(lowercase_letters)
        if upperChar == 1:
            options.append(uppercase_letters)
    else:
        return "None"
    if checkCounter == 1:
        while counter < length:
            randomChoice = secrets.choice(options)
            password.append(secrets.choice(randomChoice))
            counter += 1
    else:
        used = []
        while counter < length:
            randomChoice = secrets.choice(options)
            if randomChoice == used:
                continue
            else:
                used = randomChoice
                counter += 1
                password.append(secrets.choice(randomChoice))
    return "".join(password)
