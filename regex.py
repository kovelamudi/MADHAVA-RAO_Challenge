#!/usr/local/bin/python3
import re
valid = [] #Defining lists
invalid = []
cards = open('creditcards.txt','r') #reading the cards information
for card in cards:
    card = card.rstrip("\n")
    validity = True
    if "-" in card:  #If hyphen is in the cardnumber
        if len(card) != 19:  #Length should be 16 digits + 3 hyphens
            invalid.append({card:"Invalid Length/Incorrect Hyphen placements"})
            validity = False
        matcher = re.search("^\d{4}-\d{4}-\d{4}-\d{4}$",card) #hyphen must be followed by a four digits
        if matcher is None:
            invalid.append({card:"Invalid numbers/placements"})
            validity = False
    matcher = re.search("0{4,}|1{4,}|2{4,}|3{4,}|4{4,}|5{4,}|6{4,}|7{4,}|8{4,}|9{4,}",card) #no more 4 consecutively repeated numbers
    if matcher is not None:
        invalid.append({card:"A number repeated consecutively 4 or more times"})
        validity = False
    matcher = re.search("^[0-9-]*$",card) #Should contains only digits and hyphen
    if matcher is None:
        invalid.append({card:"Additional characters found apart from digits and hyphen"})
        validity = False
    matcher = re.search("^[4|5|6]",card) #must starts with 4/5/6
    if matcher is None:
        invalid.append({card:"Not starting with 4/5/6"})
        validity = False
    if validity:
        valid.append(card)
uniqueInvalidCards = [] #Loading the unique keys
for invalidCard in invalid:
    for key in invalidCard.keys():
        uniqueInvalidCards.append(key)
uniqueInvalidCards = set(uniqueInvalidCards)

for card in uniqueInvalidCards: #printing the invalid card numbers and their reason.  Each card may fail to satisfy multiple rules
    print ("\n",card)
    print ("----------------------------")
    for invalidCard in invalid:
        for key in invalidCard.keys():
            if key == card:
                print (invalidCard[card])

print ("\n********************")  #printing valid cards here
print ("Valid Cards Are:")
for card in valid:
    print (card)
print ("********************")
