
"""
my original idea
print("Type a number between 1 and 10")
print("Ttpe easteregg, I dare you")
ph=input("")
if ph == "7":                                   #fail
    print("That is neutral")
    sleep(1)
    print("Items include")
    sleep(1)
    print("pure water")
    sleep(1)
    print("milk")
    sleep(1)
    print("human siliva")
    sleep(1)
    print("blood")
elif ph == "6":
    print("")
"""

#this is what it will look like when you run it

"""  
['hydrochloric acid', 'upset stomach acid', 'battery acid', 'normal stomach acid', 'soadas', 'vinegar', 'lemons', 'orange juice', 'acidic soil', 'tomatoes', 'bananas', 'coffee', 'bread', 'salmon', 'potatoes', 'nomal rain', 'pure water', 'milk', 'human siliva', 'blood', 'seawater', 'eggs', 'baking soda', 'phosphate detergents', 'borax', 'antacids', 'milk of magnesia', 'ammonia', 'nonphosphate detergents', 'bleach', 'sodium hydroxide']
Type one of the words
Type easteregg, I dare you
"""

#new idea

def neverend():                         #LOL =)
    while True:
        print("This is the song that never ends")
        sleep(1)
        print("Yes it goes on and on my friend")
        sleep(1)
        print("Some people started singing it")
        sleep(1)
        print("Not knowing what it was")
        sleep(1)
        print("But people kept singing it just because")
        sleep(1)


def scal():
    print(" _________________________________________________________________________________________")   #made this myself
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |")
    print("-------------------------------------------------------------------------------------------")

scale = ['hydrochloric acid', 'upset stomach acid', 'battery acid', 'normal stomach acid', 'sodas', 'vinegar', 'lemons', 'orange juice', 'acidic soil', 'tomatoes', 'bananas', 'coffee', 'bread', 'salmon', 'potatoes', 'nomal rain', 'pure water', 'milk', 'human siliva', 'blood', 'seawater', 'eggs', 'baking soda', 'phosphate detergents', 'borax', 'antacids', 'milk of magnesia', 'ammonia', 'nonphosphate detergents', 'bleach', 'sodium hydroxide']

from time import sleep

while True:
    print(scale)
    print("Type one of the words")
    print("Type easteregg, I dare you")         #go on  
    ph=input("")

    if ph == "hydrochloric acid":
        print("0 on the pH scale")
        scal()

    elif ph == "easteregg":
        neverend()

    elif ph == "upset stomach acid":
        print("1 on the pH scale")
        scal()

    elif ph == "battery acid" or "normal stomach acid":    #this might be new, I can't remember
        print("2 on the pH scale")
        scal()

    elif ph == "sodas" or "vinegar" or "lemons":
        print("3 on the pH scale")
        scal()

    elif ph == "orange juice" or "acidic soil":
        print("4 on the pH scale")
        scal()

    elif ph == "tomatoes" or "bananas" or "coffee":
        print("5 on the pH scale")
        scal()

    elif ph == "bread" or "salmon" or "potatoes" or "nomal rain":
        print("6 on the pH scale")
        scal()

    elif ph == "pure water" or "milk" or "human siliva" or "blood":
        print("7 on the pH scale")
        print("also neutral")
        scal()

    elif ph == "seawater" or "eggs":
        print("8 on the pH scale")
        scal()

    elif ph == "baking soda" or "phosphate detergents":
        print("9 on the pH scale")
        scal()

    elif ph == "borax" or "antacids":
        print("10 on the pH scale")
        scal()

    elif ph == "milk of magnesia":
        print("11 on the pH scale")
        scal()

    elif ph == "ammonia" or "nonphosphate detergents":
        print("12 on the pH scale")
        scal()

    elif ph == "bleach":
        print("13 on the pH scale")
        scal()

    elif ph == "sodium hydroxide":
        print("14 on the pH scale")
        scal()

    else:
        print("Can you english?")    #Yes, can you?
