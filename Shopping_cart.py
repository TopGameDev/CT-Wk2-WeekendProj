# Using Python and the skills we learned over the past week, create a shopping cart program that will 
# allow a user to add and remove items to a shopping cart. The cart should keep track of the quantity 
# and price of each item.  The user should also be able to view the items that are currently in their 
# cart. The user should be able to continue to add to, remove from, and view their cart until the user 
# "quits" or "checks out". When the user quits/checks out, the program should display a receipt showing 
# the items in the cart with quantity and price and the total price.


# add to cart
# remove from cart
# view cart
# 'quit'/'checkout'
    # must show quantity, price, and total price

def add_to_cart(market, cart, department, total):
    acc_total = 0
    item = input("| What item would you like to buy?: ").lower()
    print('-------------------------------------------')
    if item in cart:
        quantity = int(input(f"| How many {item}'s do you want?: "))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        cart[item]['quantity'] += quantity
        acc_total = market[department][item] * quantity
    else:
        quantity = int(input(f"| How many {item}'s do you want?: "))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        price = market[department][item]
        acc_total = market[department][item] * quantity
        cart[item] = {'quantity': quantity, 'price': price}
    
    print(f"~ {quantity} {item}'s have been added to your cart.")
    total[0] += acc_total

def del_item(cart, total):
    leave = False
    while leave == False:
        item = input("| What item would you like to put back?: type - 'back' if you change your mind.  ").lower()
        print('-------------------------------------------')
        if item == 'back':
            break
        if item in cart:
            quantity = int(input(f"| How many {item}'s do you want to put back?: "))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            cart[item]['quantity'] -= quantity
            total[0] -= cart[item]['price'] * quantity

            print(f"~ {quantity} {item}'s have been deleted from your cart.")
            print(f"~ You have {cart[item]['quantity']} {item}'s in your cart.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        finished = input('Would you like to delete more items? (Y/N): ').lower()
        if finished == 'y':
            continue
        elif finished == 'n':
            leave = True
        else:
            while not 'y' or 'n':
                    keep_shopping = input('Invalid input, would you like to delete more? (Y/N): ').lower()
                    if keep_shopping == 'y':
                        break
                    elif keep_shopping == 'n':
                        break
            if keep_shopping == 'n':
                leave = True
        if item not in cart:
            print('This item is not in your cart. Please try again.').lower()
                    
            

    
def view_cart(cart, total):
    print('Cart items: ')
    print('------------\n')
    for key, value in cart.items():
        print(f"\t{key} - {cart[key]['price']} x{cart[key]['quantity']}\n")

    print(f"Your total is: ${total[0]:.2f}")

def checkout(cart, total):
    print('Receipt: ')
    print('------------\n')
    for key, value in cart.items():
        print(f"\t{key} - {cart[key]['price']} x{cart[key]['quantity']}: ${(cart[key]['quantity']*cart[key]['price']):.2f}\n")
    print(f"Your total is: ${total[0]:.2f}")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def shopping():
    super_market = {
        'sweets' : {
            'ice-cream' : 6.99,
            'candy' : 2.99,
        },
        'drinks' : {
            'coke' : 1.99,
            'pepsi' : 1.99,
            'root-beer' : 1.99
        },
        'snacks' : {
            'doritos' : 3.99,
            'ruffles' : 3.99,
            'lays' : 3.99
        },
        'food' : {
            'pizza' : 9.99,
            'burrito' : 6.99,
            'chicken' : 5.99
        }
    }
    shopping_cart = {}
    total = [0]
    active = True
    while active == True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("| Welcome to the Super Market! Please choose a department! |")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\t----------')
        for key, value in super_market.items():
            if key == 'food':
                print(f"\t| {key}   |")
            else:
                print(f"\t| {key} |")
        print('\t----------')
        print('------------------------------------------------')
        department = input("| What department would you like to see?: ").lower()
        print('------------------------------------------------')
        if department in super_market:
            print(f"These are the products in {department}:")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            for key, value in super_market[department].items():
                print('\t------------------')
                print(f"\t| {key} {value} ")
                print('\t------------------')
            print('************************************************')
            motion = input('"back" - Main Menu, "buy" item, "view" cart: ').lower()
            print('************************************************')
            if motion == 'back':
                continue
            elif motion == 'buy':
                add_to_cart(super_market, shopping_cart, department, total)
                while True:
                    print('*********************************************************************')
                    next = input('| "add" items, "delete" items, "view" cart, "clear" cart, or "checkout": ')
                    print('*********************************************************************')
                    if next == 'add':
                        break
                    elif next == 'delete':
                        del_item(shopping_cart, total)
                    elif next == 'view':
                        if not shopping_cart:
                            print('~ Your shopping cart is empty.')
                        else:
                            view_cart(shopping_cart, total)
                    elif next == 'clear':
                        shopping_cart.clear()
                        total[0] = 0                   
                        print('~ Your shopping cart is empty.')
                    elif next == 'checkout':
                                print("Thank you for shopping at Super Market! Here's your receipt. (:")
                                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                                checkout(shopping_cart, total)
                                break
                if next == 'checkout':
                    active = False
                                
            elif motion == 'view':
                while shopping_cart:
                    view_cart(shopping_cart, total)
                    next = input('"add" items, "delete" items, or "checkout": ').lower()
                    print('*********************************************************************')
                    if next == 'add':
                        break
                    elif next == 'delete':
                        if not shopping_cart:
                            print('~ Your shopping cart is empty.')
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        else:
                            del_item(super_market, shopping_cart, department, total) 
                    elif next == 'view':
                        if not shopping_cart:
                            print('~ Your shopping cart is empty.')
                        else:
                            view_cart(shopping_cart, total)
                    elif next == 'clear':
                        shopping_cart.clear()
                        total[0] = 0
                        if not shopping_cart:
                            print('~ Your shopping cart is empty.')                   
                    elif next == 'checkout':
                            if not shopping_cart:
                                print('~ Your shopping cart is empty.')
                                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                            else:
                                print("Thank you for shopping at Super Market! Here's your receipt. (:")
                                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                                checkout(shopping_cart, total)
                                break
                    if next == 'checkout':
                        active = False

                if not shopping_cart:
                    print('Your shopping cart is empty.')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    motion = input('Would you like to continue shopping? Y/N: ').lower()
                    if motion == 'y':
                        continue
                    elif motion == 'n':
                        print('Thank you for shopping with us! :)')
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    else:
                        while not 'y' or 'n':
                            keep_shopping = input('Invalid Item, would you like to keep shopping? Y/N: ').lower()
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                            if keep_shopping == 'y':
                                break
                            elif keep_shopping == 'n':
                                break
                        if keep_shopping == 'n':
                            active = False
                if motion == 'n':
                    active = False
                
            else:
                while not 'y' or 'n':
                    keep_shopping = input('Invalid Item, would you like to keep shopping? Y/N: ').lower()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    if keep_shopping == 'y':
                        break
                    elif keep_shopping == 'n':
                        break
                if keep_shopping == 'n':
                    active = False
        else:
            while not 'y' or 'n':
                keep_shopping = input('Invalid Item, would you like to keep shopping? Y/N: ').lower()
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                if keep_shopping == 'y':
                    break
                elif keep_shopping == 'n':
                    break
            if keep_shopping == 'n':
                active = False


shopping()