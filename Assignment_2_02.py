# Initialize an empty dictionary to store products and prices
products = {}

# Taking product details from the user
while True:
    name = input("Enter product name (or type 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    price = input(f"Enter price for {name}: ").strip()
    
    # Try converting the price to float, otherwise ask again
    try:
        products[name] = float(price)
    except ValueError:
        print("Invalid price. Please enter a numeric value.")

# Searching for product prices
while True:
    search = input("\nEnter a product name to get its price (or type 'exit' to qjjuit): ").strip()
    if search.lower() == "exit":
        break
    if search in products:
        print(f"The price of {search} is: ${products[search]:.2f}")
    else:
        print("Product not found.")
