
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resources_sufficent(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough item")
            is_enough=False
    return is_enough

def process_coin():
    print("enter your coin")
    total = int(input("how many quaret: "))* 0.25
    total += int(input("how many dimes: "))* 0.1
    total += int(input("how many nickels: "))* 0.5
    total += int(input("how many pennies: "))* 0.01
    return total

def is_transaction_successful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change=round(money_recived - drink_cost, 2)
        print(f"here is {change}$ ")
        global profit
        profit += drink_cost
        return True
    else:
        print("it is not enough money")
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
      resources[item] -= order_ingredient[item]
    print(f"here is your drink {drink_name}")  

profit=0
is_on=True
while is_on:
    guess=input("what would you like:")
    if guess == "off":
        is_on = False
    elif guess== "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {profit}$")
    else:
        drink=MENU[guess]
        if is_resources_sufficent(drink["ingredients"]):
            profit=process_coin()
            if is_transaction_successful(profit, drink["cost"]):
                make_coffee(guess, drink["ingredients"])
