import random
print("wellcome to the guess game")
print("thinking of a number between 1 to 100")
print("you have 10 attempt")

lst = list(range(1,100+1))
a=random.choice(lst)

end_game=False
while not end_game:
    for i in range(1,11):
        i -= 1
        if i ==0:
            end_game = True
            print("you lose the game")
        guess=int(input("enter your number: "))
        if guess > a:
            print("too high")
        elif guess < a:
            print("too short")
        else:
            print("you win the game")
            end_game = True

