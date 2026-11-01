
def calculate_discount(price, customer_type, coupon=None):
    if customer_type == "vip":
        price = price * 0.9
    if coupon == "NOWRUZ10":
        price = price - (price * 0.1)
    elif coupon == "SUMMER5":
        price = price * 0.95
    return price
print(calculate_discount(100, "vip")) # بدون کد تخفیف
print(calculate_discount(100, "normal", "NOWRUZ10")) # مشتری عادی با کد نوروزی
print(calculate_discount(100, "vip", "NOWRUZ10")) # مشتری VIP با کد نوروزی (تخفیف‌ها روی هم اعمال می‌شوند)
print(calculate_discount(100, "normal", "SUMMER5")) # مشتری عادی با کد تابستانه