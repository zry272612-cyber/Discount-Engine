def calculate_discount(price, customer_type, coupon=None, is_first_order=False, date=None, city=None):
    # تخفیف VIP
    if customer_type == "vip":
        price = price * 0.9
    elif customer_type == "gold":
        price = price * 0.95

    # کد تخفیف - کپی‌پیست از چند جای دیگر
    if coupon == "NOWRUZ10":
        if date and date.month == 3:
            price = price - (price * 0.1)
        else:
            pass  # TODO: این را بعداً درست کنیم
    elif coupon == "SUMMER5":
        price = price * 0.95
    elif coupon == "WELCOME20":
        if is_first_order:
            price = price * 0.8
        else:
            price = price - 1000  # هاردکد! عدد جادویی

    # تخفیف پله‌ای - شرط‌های تودرتو
    if price > 1000000:
        price = price * 0.97
    elif price > 500000:
        price = price * 0.98
    elif price > 200000:
        price = price * 0.99

    # تخفیف شهری - تعداد شهرها هر ماه زیاد می‌شود
    if city == "TEHRAN":
        price = price - 50000
    elif city == "MASHHAD":
        price = price - 30000
    elif city == "ISFAHAN":
        price = price - 25000
    # ... ۴۰ خط دیگر برای بقیهٔ شهرها

    # مالیات - کی این را اینجا گذاشت؟!
    price = price + (price * 0.09)

    return price

# سناریو ۱: مشتری VIP از تهران (بدون کد تخفیف)
print("تست ۱:", calculate_discount(100000, "vip", city="TEHRAN"))

# سناریو ۲: مشتری عادی، اولین خریدش است، از مشهد
print("تست ۲:", calculate_discount(100000, "normal", is_first_order=True, coupon="WELCOME20", city="MASHHAD"))

# سناریو ۳: خرید بالا از اصفهان (بالای ۵۰۰ هزار تومان)
print("تست ۳:", calculate_discount(600000, "gold", city="ISFAHAN"))
