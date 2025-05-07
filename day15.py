# Coffee Machine Program in Rupees


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 80,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ₹{resources['money']}")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins (₹).")
    ten = int(input("How many ₹10 coins? "))
    five = int(input("How many ₹5 coins? "))
    two = int(input("How many ₹2 coins? "))
    one = int(input("How many ₹1 coins? "))
    total = ten * 10 + five * 5 + two * 2 + one * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = money_received - drink_cost
    if change > 0:
        print(f"Here is ₹{change} in change.")
    resources['money'] += drink_cost
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


# Main loop
is_on = True
print(r"""
     ( (
      ) )
   ........
   |      |]      DIGITAL
   \\      /       COFFEE
    `----'        MACHINE
  __||__||__
 |    ☕   | [ESPRESSO]   -- 30rs
 |    ☕   | [LATTE]      -- 50rs 
 |    ☕   | [CAPPUCCINO] -- 80rs  
 |_________|   
  |      |
  |______|
 (________)
   """)

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select from espresso/latte/cappuccino.")
