import random
playing = True
number=str(random.randint(0,9))
print("i will generate a number from 0 to 9 and you have to guess the number:" )
print("the game ends when you get 1 hero ! ")
while playing :
    guess=input("give me your best guess:")
    if number ==guess:
        print("you win the game ")
        print("the number was " ,number )
        break 
    else:
        print (" your guess isnt quite right , try again ")