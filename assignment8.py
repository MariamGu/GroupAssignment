def add_product(basket):
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    if product_name in basket:
        basket[product_name]['quantity'] += quantity
        basket[product_name]['price'] = price
    else:
        basket[product_name] = {'price': price, 'quantity': quantity}
    print(f"{quantity} unit(s) of {product_name} added to the basket.")


def view_products(basket):
    if not basket:
        print("Your basket is empty.")
    else:
        for product, details in basket.items():
            print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")


def remove_product(basket):
    product_name = input("Enter product name to remove: ")
    if product_name in basket:
        del basket[product_name]
        print(f"{product_name} removed from the basket.")
    else:
        print("Product not found in the basket.")


def calculate_total(basket):
    total_cost = sum(details['price'] * details['quantity'] for details in basket.values())
    print(f"Total cost: {total_cost}")


def run_application():
    basket = {}
    while True:
        print("\nMenu:")
        print("1. Add product to basket")
        print("2. View all products in basket")
        print("3. Remove product from basket")
        print("4. Calculate total cost")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_product(basket)
        elif choice == '2':
            view_products(basket)
        elif choice == '3':
            remove_product(basket)
        elif choice == '4':
            calculate_total(basket)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


run_application()