# Step 1: Define the grocery store items and their prices
grocery_prices = {
    "apple": 0.50,
    "banana": 0.30,
    "milk": 1.20,
    "bread": 1.50,
    "eggs": 2.00,
    "rice": 0.90,
    "chicken": 5.00
}

# Step 2: Function to look up item prices
def lookup_price():
    item = input("Enter the grocery item you want the price for: ").lower()

    if item in grocery_prices:
        print(f"The price of {item} is ${grocery_prices[item]:.2f}")
    else:
        print(f"Sorry, {item} is not available in the grocery store.")

# Step 3: Main loop
while True:
    lookup_price()
    again = input("Do you want to look up another item? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for using the grocery price lookup!")
        break