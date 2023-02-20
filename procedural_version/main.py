from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
running = True
total_profit = 0


def print_report():
    for key in resources:
        measure = 'ml'
        if key == 'coffee':
            measure = 'g'
        print(f'{key.capitalize()}: {resources[key]}{measure}')
    print(f'Money : ${total_profit}')


def check_resources(user_selection):
    """Takes user selection as dict. and returns if not enough resources,
     otherwise prints the price of the selection"""
    resource_needed = MENU[user_selection]['ingredients']
    for key in resource_needed:
        if resource_needed[key] > resources[key]:
            print(f'Sorry, not enough {key}.')
            return
    price = MENU[user_selection]['cost']
    print(f'The price is ${price}')
    process_payment(user_selection)


def deduct_resources(user_selection):
    """Takes user selection as a string, and deducts used values from
     resources"""
    ingredients = MENU[user_selection]['ingredients']
    for key in ingredients:
        resources[key] -= MENU[user_selection]['ingredients'][key]
    return


def get_coin_input():
    """Prompts for 4 types of coins and returns total value collected"""
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    total_sum = 0
    for key in coins:
        quantity = int(input(f'Please insert number of {key}: '))
        total_sum += quantity * coins[key]
    return round(total_sum, 2)


def process_payment(user_selection):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    price = MENU[user_selection]['cost']
    total_inserted = get_coin_input()
    if total_inserted >= price:
        difference = round(total_inserted - price, 2)
        global total_profit
        total_profit += total_inserted - difference
        # refund
        if difference > 0:
            print(f'Here is ${round(difference, 2)} in change')
        deduct_resources(user_selection)
        print(f'Here is your {user_selection}☕, enjoy!')
    else:
        print(f'Sorry, insufficient funds. You are refunded ${round(total_inserted, 2)}.')


"""The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer."""
while running:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        exit()
    elif choice == 'report':
        print_report()
    elif choice not in ['espresso', 'latte', 'cappuccino']:
        print(f'Sorry, selected product not available.')
    else:
        check_resources(choice)
