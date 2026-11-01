def calculate_discount(price: float, customer_type: str) -> float:
    if customer_type == "vip":
        return price * 0.9
    return price
print(calculate_discount(100,"vip"))
print(calculate_discount(100,"normal"))

