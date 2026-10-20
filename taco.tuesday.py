# Taco Tuesday - Taco Palace Ordering System

def print_menu():
    """Display the Taco Palace menu."""
    print("\nTaco Palace Menu")
    print("1. Taco - $5.00")
    print("2. Burrito - $7.50")
    print("3. Nachos - $6.00")
    print("4. Soft Drink - $2.45")
    print("5. Quit")


def get_price(selection):
    """Return the price for the selected menu item."""
    if selection == 1:
        return 5.00
    elif selection == 2:
        return 7.50
    elif selection == 3:
        return 6.00
    elif selection == 4:
        return 2.45
    else:
        return 0.00


def get_item_name(selection):
    """Return the name of the selected menu item."""
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    else:
        return ""


def main():
    ordered_items = []
    total = 0.00

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    while True:
        print_menu()
        selection = int(input("Enter your selection (1-5): "))

        if selection == 5:
            break
        elif selection >= 1 and selection <= 4:
            item_name = get_item_name(selection)
            item_price = get_price(selection)
            ordered_items.append(item_name)
            total += item_price
            print(f"You have selected a {item_name}.")
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")

    print("\nYour order:")
    if len(ordered_items) == 0:
        print("You did not order any food items.")
    else:
        print(", ".join(ordered_items))
    print(f"Your total is ${total:.2f}")


if __name__ == "__main__":
    main()