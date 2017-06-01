
"""
this is going to be a text based game involving you trying to reclaim the kings treasure.
"""


from time import sleep

def gameover():
    print("        ______     ______     __    __     ______        ______     __   __   ______     ______    ")
    print("       /\  ___\   /\  __ \   /\ \-./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   ")
    print("       \ \ \____  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   ")
    print("        \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ ")
    print("         \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/ ") 

def scene1():
    sleep(1)
    print("Knight Bill: 'The King wishes to speak to you " + name + "'" )
    sleep(1)
    print("You: 1. Follow Knight Bill")
    print("You: 2. Stay here")
    ch1=input("")

    if ch1 == "follow knight bill" or "Follow Knight Bill" or "1":
        scene2()

    elif ch1 == "stay here" or "Stay here" or "2":
        print("Knight Bill: 'It is very urgent " + name + "'")
        print("1. Follow Knight Bill")
        ch2=input("")

        if ch2 == "Follow Knight Bill" or "follow knight bill" or "1":
            scene2()

        else:
            gameover()
        
        

def scene2():
    print("*You follow Knight Bill to The King's castle*")
    sleep(1)
    print("The King: 'I am so glad you could make it here " + name + "'")
    sleep(1)
    print("You: 1. 'What is the matter your highness?'")
    print("You: 2. 'I had better things to do.'")
    ch3=input("")

    if ch3 == "1":
        sleep(1)
        print("The King: 'All my treasure has gone missing, and I need you to find it!'")
        print("You: 1. 'I'm on it.'")
        print("You: 2. 'Find your own damn treasure'")

        if ch5 == "1":
            print("1. go to the dark, spooky cave that definitely has a dragon in it.")
            print("2. go to the very peacful woods")

    elif ch3 == "2":
        print("Knight Bill: 'Respect the King!'")
        sleep(1)
        print("The King: 'Now, are you going to listen to me or not?'")
        sleep(1)
        print("You: 1. 'Proceed your highness'")
        print("You: 2. 'I don't care'")
        ch4=input("")
        
        if ch4 == "1":
        	print("The King: 'All my treasure has gone missing, and I need you to find it!'")

        elif ch4 == "2":
              print("The King: 'Throw him in jail!'")
              gameover()

        
            




print("Welcome, player")
print("Type numbers")
print("New Game")
print("Quit Game")
menu=input("")

if menu == "new game" or "New Game":
    print("Insert name here:")
    name=input("")

    scene1()

    

elif menu == "quit game" or "Quit Game":
    print("Program terminated")
