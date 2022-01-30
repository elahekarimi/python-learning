from art import logo
from game_data import data
from art import vs
import random
import os
clear = lambda: os.system('cls')

score=0
def check_answer(guss,a_follower_count,b_follower_count ):
    if a_follower_count > b_follower_count:
        return guss=="a"
    else:
        return guss=="b"


game_should_continue=True
while game_should_continue:
    print(logo)
    # compareA = compareB
    # compareb=random.choice(data)

    compareA=random.choice(data)
    compareB=random.choice(data)
    if compareA == compareB:
        compareB = random.choice(data)

    compare_name=compareA["name"]
    compare_follower_count=compareA["follower_count"]
    compare_description=compareA["description"]
    compare_country=compareA["country"]
    print(f"compareA: {compare_name}, {compare_follower_count}, {compare_description}, {compare_country}")
    print(vs)

    compare_nameb=compareB["name"]
    compare_follower_countb=compareB["follower_count"]
    compare_descriptionb=compareB["description"]
    compare_countryb=compareB["country"]
    print(f"compareB: {compare_nameb}, {compare_follower_countb}, {compare_descriptionb}, {compare_countryb}")

    guss=input("enter your guss a or b: ")
    a_follower_count= compareA["follower_count"]
    b_follower_count= compareB["follower_count"]
    is_correct=check_answer(guss, a_follower_count, b_follower_count)
    clear()
    if is_correct:
        score += 1
        print(f"true, your score {score} ")
    else:
        game_should_continue = False
        print(f"false, your score {score}")

