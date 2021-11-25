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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 7 Make Coffee

def update_resource(user_coffee_choice):
    global resources
    for ingredient in MENU[user_coffee_choice]['ingredients']:
        resources[ingredient] -= MENU[user_coffee_choice]['ingredients'][ingredient]


# TODO: 3 Print report of all coffee machine resources

def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


# TODO: 4 Check resources sufficient

def check_resources(drink):
    for resource in MENU[drink]['ingredients']:
        print(resource)
        if resources[resource] < MENU[drink]['ingredients'][resource]:
            print(f"There's no enough {resource}")
            return False
    return True


# TODO: 5 Process Coins

def process_coins():
    print('Please insert coins.')
    quarters = float(input('how many quarters '))
    dimes = float(input('how many dimes '))
    nickles = float(input('how many nickles '))
    pennies = float(input('how many pennies '))
    total = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    return round(total, 2)


# TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

machine_on = True

while machine_on:
    users_choice = input('What would you like? (espresso/latte/cappuccino)')
    # TODO: 2 Turn off the Coffee Machine by entering "off" to the prompt
    if users_choice == 'off':
        machine_on = False
    elif users_choice == 'report':
        print_report()
    else:
        sufficient_resource = check_resources(users_choice)
        if sufficient_resource:
            total_money = process_coins()
        # TODO: 6 Check transaction successful
            if total_money >= MENU[users_choice]["cost"]:
                update_resource(users_choice)
                change = 0
                if total_money > MENU[users_choice]["cost"]:
                    change = round((total_money-MENU[users_choice]["cost"]), 2)
                    print(f'Here is {change} dollars in change')
                money += total_money-change
                print(f'Here is your {users_choice}. Enjoy')
            else:
                print("Sorry that's not enough money. Money refunded.")
