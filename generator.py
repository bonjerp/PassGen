import random
import string

from config import PUNCTUATION, CONFUSING_COMBO


def hasConfusingCombo(password):
    for i in range(1, len(password)):
        if password[i - 1] in CONFUSING_COMBO and password[i] in CONFUSING_COMBO:
            return True

    return False

def generatePassword(length, useUpper=True,useLower=True,useNumbers=True, useSymbols=True, minNumbers=0, minSymbols=0):
    characters = ""
    numbers = string.digits
    symbols = PUNCTUATION

    if useUpper:
        characters += string.ascii_uppercase

    if useLower:
        characters += string.ascii_lowercase

    if useNumbers:
        characters += numbers

    if useSymbols:
        characters += symbols
        
    if not characters:
        return "Pick at least one character type."

    if minNumbers + minSymbols > length:
        return "Minimums are bigger than password length."
    
    if minNumbers > 0 and not useNumbers:
        return "Numbers are disabled."
    
    if minSymbols > 0 and not useSymbols:
        return "Symbols are disabled."
    
    password = []

    for i in range(minNumbers):
        password.append(
            random.choice(numbers)
        )

    for i in range(minSymbols):
        password.append(
            random.choice(symbols)
        )
        
    while len(password) < length:
        password.append(
            random.choice(characters)
        )

    while True:
        random.shuffle(password)
        finalPassword = "".join(password)
        if not hasConfusingCombo(finalPassword):
            return finalPassword