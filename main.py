class CoffeeShop:
    def __init__(self):
        # Initialize the menu with available items and their prices
        self.menu = {
            "tea": 2.5,
            "cappuccino": 2.0,
            "black coffee": 3.5,
            "latte": 3.0,
            "cold brew": 4.0,
            "barista": 1.25
        }

        # Initialize the inventory with available stock for each item
        self.inventory = {
            "tea": 10,
            "cappuccino": 10,
            "black coffee": 10,
            "latte": 10,
            "cold brew": 10,
            "barista": 20
        }

        # Initialize total sales to 0
        self.sales = 0.0
        # To store the customer’s name
        self.customer_name = ""
        # To store the current order items and their quantities
        self.current_order = {}  # Dictionary to track current orders

    def display_menu(self):
        """Display the coffee shop menu."""
        print("\n---- Menu ----")
        # Loop through the menu dictionary and display each item with its price
        for item, price in self.menu.items():
            print(f"{item.capitalize()} : ${price:.2f}")
        print("------------------\n")

    def take_order(self):
        """Take orders from the customer, allowing multiple items."""
        # Clear the current order in case there was a previous one
        self.current_order.clear()

        # Start a loop to take multiple orders
        while True:
            # Display the menu before each order
            self.display_menu()
            # Prompt the customer to place an order or type 'done' to finish ordering
            order = input(f"{self.customer_name}, what would you like to order? (or type 'done' to finish) ").lower()

            # If the customer is done ordering, break the loop
            if order == 'done':
                break

            # Check if the ordered item exists in the menu
            if order in self.menu:
                # Check if there is enough inventory for the item
                if self.inventory[order] > 0:
                    # Ask the customer for the quantity they want
                    quantity = int(input("How many would you like? "))

                    # Check if the requested quantity is available
                    if quantity <= self.inventory[order]:
                        # Add the item and quantity to the current order
                        if order in self.current_order:
                            # If the item is already in the order, increase the quantity
                            self.current_order[order] += quantity
                        else:
                            # Otherwise, add the item with the quantity
                            self.current_order[order] = quantity
                    else:
                        # Notify the customer if the requested quantity exceeds the available stock
                        print(f"Sorry, we only have {self.inventory[order]} {order}(s) left.")
                else:
                    # Notify the customer if the item is out of stock
                    print(f"Sorry, we're out of {order}.")
            else:
                # Notify the customer if the item is not on the menu
                print(f"Sorry, {order} is not on the menu.")

        # Once all orders are taken, process the order
        self.process_order()

    def process_order(self):
        """Calculate the total cost, display the order summary, and confirm the order."""
        total_cost = 0.0  # Initialize the total cost for the current order
        print("\n--- Order Summary ---")

        # Loop through the current order dictionary to calculate the total and print details
        for item, quantity in self.current_order.items():
            cost = self.menu[item] * quantity  # Calculate cost for each item
            total_cost += cost  # Add the item cost to the total cost
            # Print the item, quantity, and cost
            print(f"{quantity} x {item.capitalize()} = ${cost:.2f}")

        # Display the total cost of the order
        print(f"Total cost: ${total_cost:.2f}")
        print("---------------------\n")

        # Ask the customer to confirm the order
        confirm = input("Would you like to proceed with the order? (yes/no) ").lower()

        # If the customer confirms, update sales and inventory
        if confirm == "yes":
            # Add the total cost to the total sales
            self.sales += total_cost
            # Deduct the ordered quantities from the inventory
            for item, quantity in self.current_order.items():
                self.inventory[item] -= quantity
            # Thank the customer
            print(f"Thank you, {self.customer_name}. Your order has been placed.")
        else:
            # Notify the customer if the order was canceled
            print("Order cancelled.")

    def display_sales(self):
        """Display the total sales made so far."""
        print(f"\nTotal Sales: ${self.sales:.2f}")

    def display_inventory(self):
        """Display the remaining inventory for each item."""
        print("\n--- Inventory ---")
        # Loop through the inventory and display the item and the remaining quantity
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")
        print("-------------------\n")

    def main(self):
        """Main program loop to handle the user interaction."""
        # Ask for the customer’s name at the start
        self.customer_name = input("Welcome to CoffeeShop! May I have your name? ").capitalize()
        print(f"Hello, {self.customer_name}! It's great to have you here.")

        # Start an infinite loop for the main menu
        while True:
            # Display the main menu options
            print(f"\n{self.customer_name}, please choose an option:")
            print("1. Place order")
            print("2. View Sales")
            print("3. View Inventory")
            print("4. Exit")

            # Ask the customer to choose an option
            choice = input("Please select an option: ")

            # Depending on the customer’s choice, execute the appropriate method
            if choice == "1":
                self.take_order()  # Take an order
            elif choice == "2":
                self.display_sales()  # Display total sales
            elif choice == "3":
                self.display_inventory()  # Display inventory
            elif choice == "4":
                # Exit the program and thank the customer
                print(f"Thank you for visiting our shop, {self.customer_name}. Karibu tena 🫶🏾")
                break  # Exit the loop to terminate the program
            else:
                # Handle invalid input by displaying an error message
                print("Invalid choice. Please select a valid option.")

# Ensure the program runs only when executed directly, not when imported
if __name__ == "__main__":
    # Create an instance of CoffeeShop and start the main program loop
    shop = CoffeeShop()
    shop.main()
