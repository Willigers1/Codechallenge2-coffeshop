class CoffeeShop:
    def __init__(self):
       
        self.menu = {
            "tea": 2.5,
            "cappuccino": 2.0,
            "black coffee": 3.5,
            "latte": 3.0,
            "cold brew": 4.0,
        }
    
        self.inventory = {
            "tea": 10,
            "cappuccino": 10,
            "black coffee": 10,
            "latte": 10,
            "cold brew": 10
        }
       
        self.sales = 0.0
       
        self.customer_name = ""

   
    def display_menu(self):
        print("\n---- Menu ----")
        # Loop through the menu items and display them with prices
        for item, price in self.menu.items():
            print(f"{item.capitalize()} : ${price:.2f}")
        print("------------------\n")

    # How the customers order will be taken 
    def take_order(self):
        # Display the menu before asking for an order
        self.display_menu()
        # Ask the customer what they want to order
        order = input(f"{self.customer_name}, what would you like to order? ").lower()

        # Checking if the order placed is in the menu 
        if order in self.menu:
            # Check if the ordered item is available in inventory
            if self.inventory[order] > 0:
                # Ask for the quantity the customer wants
                quantity = int(input("How many would you like? "))
                # Check if the requested quantity is available in inventory
                if quantity <= self.inventory[order]:
                    # Process the order if enough quantity is available
                    self.process_order(order, quantity)
                else:
                    # Inform the customer if the quantity requested exceeds available stock
                    print(f"Sorry, we only have {self.inventory[order]} {order}(s) left.")
            else:
                # Inform the customer if the item is out of stock
                print(f"Sorry, we're out of {order}.")
        else:
            # Inform the customer if the item is not on the menu
            print(f"Sorry, {order} is not on the menu.")

    # Method to process the order after confirming availability
    def process_order(self, order, quantity):
        # Calculate the total cost of the order
        cost = self.menu[order] * quantity
        # Display the order summary and total cost to the customer
        print(f"Your order: {quantity} {order}(s) for ${cost:.2f}")
        # Ask the customer to confirm the order
        confirm = input("Would you like to proceed with the order? (yes/no) ").lower()
        
        # If the customer confirms, update sales and inventory
        if confirm == "yes":
            self.sales += cost  # Add the cost to total sales
            self.inventory[order] -= quantity  # Deduct the ordered quantity from inventory
            print(f"Thank you, {self.customer_name}. Your order for {quantity} {order}(s) has been placed.")
        else:
            # If the customer cancels, display a message
            print("Order cancelled.")

    # Method to display the total sales made
    def display_sales(self):
        print(f"\nTotal Sales: ${self.sales:.2f}")

    # Method to display the current inventory status
    def display_inventory(self):
        print("\n--- Inventory ---")
        # Loop through the inventory and display the available quantity of each item
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")
        print("-------------------\n")

    # Main menu loop to handle user interaction with the system
    def main(self):
        # Ask for the customer's name at the start of the program
        self.customer_name = input("Welcome to CoffeeShop! May I have your name? ").capitalize()
        print(f"Hello, {self.customer_name}! It's great to have you here.")

        while True:
            # Display the main menu options
            print(f"\n{self.customer_name}, please choose an option:")
            print("1. Place order")
            print("2. View Sales")
            print("3. View Inventory")
            print("4. Exit")
            
            # Ask the user to select an option
            choice = input("Please select an option: ")

            # Execute the appropriate function based on user choice
            if choice == "1":
                self.take_order()  # Place an order
            elif choice == "2":
                self.display_sales()  # View total sales
            elif choice == "3":
                self.display_inventory()  # View current inventory
            elif choice == "4":
                # Exit the program with a thank you message
                print(f"Thank you for visiting our shop, {self.customer_name}. Karibu tena 🫶🏾")
                break  # Exit the loop to end the program
            else:
                # Handle invalid menu choices
                print("Invalid choice. Please select a valid option.")

# Ensure this code runs only when the script is executed directly, not when imported
if __name__ == "__main__":
    # Create an instance of CoffeeShop and start the main menu loop
    shop = CoffeeShop()
    shop.main()
