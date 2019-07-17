'''
The purpose of this program is to show how honey encryption
works. Given any password, the program should be able to
give the user a selection of manipulated passwords (sweet
words). If the sweet word is entered, then the program will
trigger an alarm. Of course, the correct password will
not trigger the alarm.
'''
import random
from pprint import 

def validate(char):

	while char != 'Y' and char != 'y' and char != 'N' and char != 'n':
            char = input("Would you like to enter another inquiry? (Y/N) ")

while True:
    userPass = input("Please enter a password: ")
    message = input("Please enter a secret message to store (one word): ")
    passwordsToSeeds = {}   # dictionary
    trueSeed = random.randint(10, 27)    # Random seed value

    ' Verify input with the user '
    print("Your password is " + userPass
          + ", your seed value is " + str(trueSeed)
          + ", and your secret message is " + message
          + "\n=====================================")

    passwordsToSeeds[userPass] = trueSeed
    passwordsToSeeds[userPass + str(trueSeed - 1)] = trueSeed + 1
    passwordsToSeeds[userPass + str(trueSeed - 2) + "1"] = trueSeed + 2
    passwordsToSeeds[userPass.lower()] = trueSeed + 3
    passwordsToSeeds[userPass.lower() + str(trueSeed + 1) + "3"] = trueSeed + 4
    passwordsToSeeds[userPass.upper()] = trueSeed + 5
    passwordsToSeeds[userPass.upper() + str(trueSeed + 2) + "5"] = trueSeed + 6
        # ENCRYPTION: c = sk XOR sm
    cipher = int(passwordsToSeeds[userPass]) ^ trueSeed

    passwords = list(passwordsToSeeds.keys())
    random.shuffle(passwords)                   # Shuffle the passwords
    pprint(passwords)                           # Display results

    try:
        query = input("Enter a password to crack: ")
        keySeed = passwordsToSeeds[query]
        # DECRYPTION: m = sk XOR c
        m = keySeed ^ cipher                        # ^ == XOR

        if m != trueSeed:                       # Honey checker
            print("Intruder! SOUNDING ALARM!")  # If seeds don’t match, this is an intruder

        pprint(seedsToMessages[m])
    except KeyError:
        print("Password not found. ")

    retry = input("Would you like to enter another inquiry (Y/N):  ")
    validate(retry)  # Validates input

    if retry == 'N' or retry == 'n':
        break

print("\nThank you for testing Honey Encryption")

'''
    DEBUGGING
    print(str(cipher) + "\n" +
          str(int(passwordsToSeeds[userPass])) + "\n" +
          str(trueSeed))
    print("\n" + str(m) + "\n" +
          str(keySeed) + "\n" +
          str(cipher))
    for x in seedsToMessages.keys():           # Display results
        print(str(x) + "\t" + str(seedsToMessages[x]))
'''
