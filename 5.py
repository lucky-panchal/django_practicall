class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {
                "price": price,
                "quantity": quantity
            }
        print(f"{quantity} x {name} added to cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from cart.")
        else:
            print("Item not found in cart.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def display_cart(self):
        print("\nShopping Cart:")
        for name, item in self.items.items():
            subtotal = item["price"] * item["quantity"]
            print(f"{name}: {item['quantity']} x ₹{item['price']} = ₹{subtotal}")

        print(f"Total Price: ₹{self.calculate_total()}")


# Create a shopping cart object
cart = ShoppingCart()

# Add items
cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1500, 1)

# Display cart
cart.display_cart()

# Remove an item
cart.remove_item("Mouse")

# Display updated cart
cart.display_cart()