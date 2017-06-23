from random import randint, choice, shuffle

cardOriginal = 3456124561942119
expiryOriginal = "03/05/2019"
# userNames = ['Rohit Kumar', 'Kritika Agarwal', 'Abhinav Jha', 'Harish Vanjetramat', 'Bhavana Gudi', 'Prithvi Prakash', 'Aishawarya Gunasekar', 'Anant Sandaliya', 'Gagan Jain', 'Sanskar Gupta', 'Rajeev Kumar Singh', 'Shalu Agarwal', 'Pooja Priya Sharma', 'Ankur Prasun', 'Ankit Bharadwaj']

def randdomize_card_mid(n):
	rangeStart = 10**(n-1)
	rangeEnd = (10**n)-1
	return randint(rangeStart, rangeEnd)

def random_year():
	return randint(2017, 2036)

def random_month():
	return randint(1,12)

def random_day():
	year = random_year()
	month = random_month()
	if month == 2:
	    if year%4 == 0:
	        return randint(1,29)
	    else:
	        return randint(1,28)
	elif month in [2,4,6,9,11]:
	    return randint(1,30)
	elif month in [1, 3, 5, 7, 8, 10, 12]:
	    return randint(1,31)


def card_number_randomizer():
    # cardOriginal = int(input("Enter a 16 digit card number: "))
    # expiryOriginal = str(input("Enter expiry date in format 'dd/mm/yyyy': "))
    userNames=['rohit']
    cardString = str(cardOriginal)
    cardFirst = cardString[:4]
    cardLast = cardString[-4:]
    expiryDay = expiryOriginal[:2]
    expiryMonth = expiryOriginal[3:5]
    expiryYear = expiryOriginal[-4:]
    randomExpiryDate = []
    randCardNumber = []
    # randCardNumber = [str(randdomize_card_mid(8)) for i in range(len(honeyElements))]
    randomExpiryDate = [str(random_day()) + "/" + str(random_month()) + "/" + str(random_year()) for i in range(6)]
    randCardNumber = [str(randdomize_card_mid(8)) for i in range(6)]
    cardPossible = [cardFirst + i + cardLast for i in randCardNumber]
    # shuffledUserNames = [ i for i in userNames]
    # shuffle(shuffledUserNames)
    # randUserNames = shuffledUserNames[:6]
    # print(cardPossible)
    # print(randomExpiryDate)
    cardDetails = [list(i) for i in zip(cardPossible, randomExpiryDate)]
    # print(cardDetails)
    # print(choice(cardDetails))
    card = choice(cardDetails)
    # print(card)
    data = [list(i) for i in zip(userNames, card)]
    # print(card.append(userNames))
    print(data) 


card_number_randomizer()
