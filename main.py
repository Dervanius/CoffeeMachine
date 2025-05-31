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


def check_resources(drink, material):
    for substance in MENU[drink]["ingredients"]:
        # print(substance)
        if MENU[drink]["ingredients"][substance] > material[substance]:
            print(f"Sorry, there is no more {substance}.\nPlease contact support.")
            return False
    print(f"One {drink} coming right up!\nShow me the money!")
    return True


def deduct_resources(drink, material):
    for substance in MENU[drink]["ingredients"]:
        material[substance] -= MENU[drink]["ingredients"][substance]
        print(material[substance])


def initial_selection():
    selection = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    return selection


def status():
    print(f"Milk: {resources["milk"]} ml")
    print(f"Water: {resources["water"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"House score: ${house_score}")


def payment(unit, value, paid):
    balance = int((input(f"How manu {unit}? "))) * value
    paid = balance
    return round(paid,2)


is_machine_on = True
house_score = 0

while is_machine_on:
    working_mode = True

    while working_mode:
        choice = initial_selection()

        if choice == "off":
            print("I'm shutting down. Bye, bye!")
            working_mode = False
            is_machine_on = False
        elif choice == "report":
            status()
            working_mode = False
            is_machine_on = False
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            double_check = check_resources(choice, resources)
            if not double_check:
                working_mode = False
            else:
                customer_score = 0
                customer_score += payment("quarters", 0.25, customer_score)
                print(f"Money paid: ${round(customer_score, 2)}")
                customer_score += payment("dimes", 0.10, customer_score)
                print(f"Money paid: ${round(customer_score, 2)}")
                customer_score += payment("nickles", 0.05, customer_score)
                print(f"Money paid: ${round(customer_score, 2)}")
                customer_score += payment("pennies", 0.01, customer_score)
                print(f"Money paid: ${round(customer_score, 2)}")
                # house_score += customer_score

                if MENU[choice]["cost"] < customer_score:
                    calculate_change = customer_score - MENU[choice]["cost"]
                    print(f"Here is your change: ${calculate_change}")
                    customer_score -= calculate_change
                    print(f"Money paid: ${customer_score}")

                if MENU[choice]["cost"] == customer_score:
                    house_score += customer_score
                    print(f"You've ${customer_score} paid and you deserve {choice}")
                    deduct_resources(choice, resources)
                else:
                    print("You are too poor. Next...")
                    working_mode = False


        else:
            print(f"Sorry, we don't serve {choice}. Try again")
            working_mode = False
