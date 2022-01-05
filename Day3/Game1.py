print('wellcome to tresure Iland ')
print('your mission is find the tresure')
choose1= input('where do you whant to go? you can choose "left" or "right"').lower()
if choose1 == 'left':
    choose2=input('you come to the lake, type "wait" for wait for boat or type "swim" ').lower()
    if choose2 == "wait":
        choose3 = input ('you have to choose a door "blue", "green", "red"').lower()
        if choose3 == "green":
            print('you are wining')
        else:
                print('Game over')
else:
    print('Game over')