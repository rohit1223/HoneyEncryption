from random import randint

year = 2016
month = 4
if month == 2:
    if year%4 == 0:
        x = randint(1,29)
    else:
        x = randint(1,28)
        print ("feb no leap")
elif month in [2,4,6,9,11]:
    x =  randint(1,30)
    print("30 days")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    x = randint(1,31)
