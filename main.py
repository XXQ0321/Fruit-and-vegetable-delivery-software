# main.py

from products import Product, ProductManager
from order import Order
from user import User

def main():
    product_manager = ProductManager()
    
    # Add some initial products
    product_manager.add_product(Product("Apple", 1.00, 50))
    product_manager.add_product(Product("Banana", 0.50, 100))
    product_manager.add_product(Product("Orange", 0.80, 75))

    user_name = input("Enter your name: ")
    user = User(user_name)

    print(f"\nWelcome, {user}!\n")
    
    while True:
        print("\nAvailable Products:")
        for product in product_manager.list_products():
            print(product)

        order = Order()
        
        while True:
            product_name = input("\nEnter the product name to add to your order (or 'done' to finish): ")
            if product_name.lower() == 'done':
                break
            
            product = product_manager.find_product(product_name)
            if product:
                quantity = int(input(f"Enter quantity for {product_name}: "))
                order.add_item(product, quantity)
            else:
                print(f"{product_name} not found.")

        print(f"\nYour Order:\n{order}")

        if input("\nWould you like to place another order? (yes/no): ").lower() != 'yes':
            print("Thank you for using the grocery delivery system!")
            break

if __name__ == "__main__":
    main()
