import random
from art import logo
print(logo)
print("wellcome to the guess game")
print("thinking of a number between 1 to 100")
print("you have 10 attempt")

lst = list(range(1,100+1))
a=random.choice(lst)

end_game=False
while not end_game:
    for guess in range(1,6):
        guess -= 1
        if guess ==0:
            print("you lose the game")
            end_game = True
        guess=int(input("enter your number: "))
        if guess > a:
            print("too high")
        elif guess < a:
            print("too short")
        else:
            end_game = True
            print("you win the game")
            
            

