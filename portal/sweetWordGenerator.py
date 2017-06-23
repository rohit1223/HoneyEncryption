import random
from pprint import pprint


# while True:
# userPass = input("Please enter a password: ")
# message = input("Please enter a secret message to store (one word): ")
def sweetwords(userPass):

    passwordsToSeeds = {}   # dictionary

    # Seed generator + Sweetwords generator
    # Manipulate the password input by the user
    #   Add a string to that password
    #   Seeds should remain as integers that
    #   be converted into binary digits

    # for x in xrange(1,10):
    #     pass

    trueSeed = random.randint(17, 91)    # Random seed value
    passwordsToSeeds[userPass] = trueSeed
    passwordsToSeeds[userPass + str(trueSeed - 1)] = trueSeed + 1
    passwordsToSeeds[userPass + str(trueSeed - 2) + "1"] = trueSeed + 2
    passwordsToSeeds[userPass.lower()] = trueSeed + 3
    passwordsToSeeds[userPass.lower() + str(trueSeed + 1) + "3"] = trueSeed + 4
    passwordsToSeeds[userPass.upper()] = trueSeed + 5
    passwordsToSeeds[userPass.upper() + str(trueSeed + 2) + "5"] = trueSeed + 6
        # ENCRYPTION: c = sk XOR sm
    cipher = int(passwordsToSeeds[userPass]) ^ trueSeed

        # Shuffle the passwords and display them on the screen to begin the game
    passwords = list(passwordsToSeeds.keys())
    random.shuffle(passwords)                   # Shuffle the passwords
    # pprint(passwords)
    for password in passwords:
        target = open('password/alia.txt', 'a')
        target.write(password+'\n')
        target.close()

# sweetwords(userPass)