# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CreditCard
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from random import randint, choice, shuffle
import random


def index(request):
    return render(request, "index.html")

def vault(request, type):
    return render(request, "vault.html", {"type": type, "cards": CreditCard.objects.all()})

def detail(request, type, vault_type):
    return render(request, "form.html", {"type": type, "vault_type": vault_type})

def terminal(request, type, vault_type):
    return render(request, "terminal.html", {"type": type, "vault_type": vault_type})

def auth(request, type):
    return render(request, "auth.html", {"type": type})

cardOriginal = 3456124561942119
expiryOriginal = "03/05/2019"
# userNames = ['Rohit Kumar', 'Kritika Agarwal', 'Abhinav Jha', 'Harish Vanjetramat', 'Bhavana Gudi', 'Prithvi Prakash', 'Aishawarya Gunasekar', 'Anant Sandaliya', 'Gagan Jain', 'Sanskar Gupta', 'Rajeev Kumar Singh', 'Shalu Agarwal', 'Pooja Priya Sharma', 'Ankur Prasun', 'Ankit Bharadwaj']

def randdomize_card_mid(n):
    rangeStart = 10**(n-1)
    rangeEnd = (10**n)-1
    return randint(rangeStart, rangeEnd)

def random_year():
    return randint(2019, 2036)

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

def card_number_randomizer(userNames):
    # cardOriginal = int(input("Enter a 16 digit card number: "))
    # expiryOriginal = str(input("Enter expiry date in format 'dd/mm/yyyy': "))
    userName=[userNames]
    print(userName)
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
    print(card)
    data = userName + card 
    # print(card.append(userNames))
    print(data) 

def sweetwords(userPass, vault_type):
    passwordsToSeeds = {}
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
    passwords = list(passwordsToSeeds.keys())
    random.shuffle(passwords) 
    check_vault = 'v1'
    if vault_type == check_vault:
        # for password in passwords:
        target = open(os.path.join(settings.PASSWORD_ROOT, 'alias_v1.txt'), 'a')
        target.write(userPass+'\n')
    else:
        for password in passwords:
            target = open(os.path.join(settings.PASSWORD_ROOT, 'alias_v2.txt'), 'a')
        # target = open('password/alia.txt', 'a')
            target.write(password+'\n')
        target.close()


def passwordCreator(alias, password):
    target = open(os.path.join(settings.PASSWORD_ROOT, 'password.txt'), 'a')
    target.write(alias+':'+password+'\n')
    target.close()

@csrf_exempt
def search(request):
    check = open(os.path.join(settings.PASSWORD_ROOT, 'alias_v2.txt'), 'r')
    checklist = check.readlines()
    check.close()
    try:
        card = CreditCard.objects.get(alias=request.POST.get("search_alias",None))
        print(check_password(request.POST.get("search_password",None), card.password))
        if check_password(request.POST.get("search_password",None), card.password):
            passwordCreator(card.alias, card.password)
            return render(request, 'display.html', {"type": type, "card": card})
        else:
            print('value ValueError')
            return HttpResponse("Wrong Password")
    except CreditCard.DoesNotExist:
        print("No MyModel matches the given query.")
        for line in checklist:
            if str(request.POST.get("search_alias")+'\n') in line:
                userName = request.POST.get("search_alias")
                print(userName)
                card_number_randomizer(userName)
                print('found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            else:
                print('notfound!!!!!!!!!!!!')
        return HttpResponse("Not Found")

        
@csrf_exempt
def submit(request):
    cc = CreditCard(
        alias=request.POST.get("cc_alias",None),
        name=request.POST.get("cc_name", None),
        number=request.POST.get("cc_number", None),
        expiry_date=request.POST.get("cc_expiry_date", None),
        password=make_password(request.POST.get("password", None)),
        type=request.POST.get("type", None),
        vault_type=request.POST.get("vault_type", None),
    )
    passwordCreator(cc.alias, cc.password)
    sweetwords(cc.alias, cc.vault_type)

    cc.save();
    return redirect('/vault/'+request.POST.get("type", None))




