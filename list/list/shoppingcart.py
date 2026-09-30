cart = ["Milk", "Bread", "Apple"]
cart.append("Rice")
cart.remove("Bread")
if "Apple" in cart:
    print("Apple is available")
else:
    print("Apple is not available")
print("Shopping cart:", cart)
print("Total items:", len(cart))