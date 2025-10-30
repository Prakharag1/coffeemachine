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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_suff(order_ingredients):
    is_enough = True

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry their is no enough {item}.")
            is_enough = False
    return is_enough


def process_coin():
    print("please enter coin")
    total = int(input("How many quater")) * 0.25
    total += int(input("How many dimes")) * 0.1
    total += int(input("How many nickles")) * 0.05
    total += int(input("How many pennies")) * 0.01
    return total


def is_trans_succ(money_rec, cost):
    if money_rec >= cost:
        change = round(money_rec - cost, 2)
        print(f"Kindly recieved ${change} in change")
        global profit
        profit += cost
        return True
    else:
        print("sorry not enough money,Money refunded ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on == True:
    choice = input("what would you like ?(espresso/Latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == ("report"):

        print(f"Water: {resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee::{resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_suff(drink["ingredients"]):
            payment = process_coin()
            if is_trans_succ(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
