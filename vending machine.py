 # Inventory of the snack vending machine
inventory = [
    {'code': 'A1', 'name': 'Potato Chips', 'price': 3.5, 'stock': 10},
    {'code': 'A2', 'name': 'Chocolate Bar', 'price': 2.5, 'stock': 15},
    {'code': 'B1', 'name': 'Cookies', 'price': 4.0, 'stock': 8},
    {'code': 'B2', 'name': 'Popcorn', 'price': 3.0, 'stock': 12},
    {'code': 'C1', 'name': 'Granola Bar', 'price': 3.5, 'stock': 7},
    {'code': 'C2', 'name': 'Peanuts', 'price': 2.0, 'stock': 20},
]

def display_inventory():
    """Display the available snacks in the vending machine"""
    print("\n=======================================")
    print("       SNACK VENDING MACHINE")
    print("=======================================")
    print("Code | Snack          | Price (AED) | Stock")
    print("-----|----------------|-------------|-------")
    for item in inventory:
        print(f"{item['code']}   | {item['name'][:14]:<14} | {item['price']:>8.2f}   | {item['stock']}")

def find_item(code):
    """Find a snack by its code"""
    for item in inventory:
        if item['code'].upper() == code.upper():
            return item
    return None

def make_payment(item):
    """Handle cash payment for the selected snack"""
    print(f"\nYou selected: {item['name']} - AED {item['price']:.2f}")
    
    while True:
        try:
            cash = float(input("Insert cash (AED): "))
            if cash < item['price']:
                print(f"Not enough money. Please insert at least AED {item['price']:.2f}")
                continue
                
            change = cash - item['price']
            if change > 0:
                print(f"Your change: AED {change:.2f}")
                
            item['stock'] -= 1
            print(f"\nEnjoy your {item['name']}!")
            return True
            
        except ValueError:
            print("Invalid amount. Please enter numbers only.")

def vending_machine():
    """Main function to run the vending machine"""
    while True:
        display_inventory()
        
        # Get snack selection
        selection = input("\nEnter snack code (or 'Q' to quit): ").strip()
        if selection.upper() == 'Q':
            print("\nThank you for using our vending machine!")
            break
            
        snack = find_item(selection)
        
        if not snack:
            print("Invalid code. Please try again.")
            continue
            
        if snack['stock'] <= 0:
            print(f"Sorry, {snack['name']} is out of stock.")
            continue
            
        make_payment(snack)
        
        # Ask if user wants another snack
        another = input("\nWould you like another snack? (Y/N): ").upper()
        if another != 'Y':
            print("\nThank you for your purchase! Have a nice day!")
            break

# Start the vending machine
vending_machine() 