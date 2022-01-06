import random
number= int(input('enter a number, 0 for rock, 1 for paper, 2 for scissors:'))
random_num=int(random.randint(0, 2))
#if you choose 0 and computer choose 1: the computer win but 
#but if the computer choose 2: you win
if number == 0 and random_num == 1:
    print("the computer win you");
elif number == 0 and random_num == 2:
    print("you win")
##if you choose 1 and computer choose 2: the computer win but 
#but if the computer choose 0: you win
if number == 1 and random_num == 2:
    print("the computer win you");
elif number == 1 and random_num == 0:
    print("you win")
##if you choose 2 and computer choose 0: the computer win but 
#but if the computer choose 1: you win
if number == 2 and random_num == 0:
    print("the computer win you");
elif number == 2 and random_num == 1:
    print("you win")

    
