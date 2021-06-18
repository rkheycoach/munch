'''
Munch app will help in selecting your fav dishes
by RK
'''
# imports
from random import choice
# A. functions
#   A1. choose dishes function

def chooseDishes (days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)

    '''
    1. choose random dish from food we like - done? 
    2. check if dish hasn't been chosen, if not add to myMenu
    3. Repeat until we have required # of dishes in myMenu - done
    '''

#   A2. build shopping list function
#----------------------------------------
#B. lists
foodWeLike = ["Burger", "Pizza", "Omlette", "Stir Fry", "Paratha", "Dal Khichdi", "Curry"]
myMenu = []

#----------------------------------------
# 1. how many days to plan?
print("Hello, I'm Much, I'll help to plan your dinner menu...")
answer = input("how many days?  ")
print("okay, I'll plan for " + str(answer) + " dinners from your fav meal list")


#----------------------------------------
#2. choose dishes
chooseDishes(answer)
print ("Here's your menu...")
print("")
print(myMenu)
#----------------------------------------
#3. build a shopping list