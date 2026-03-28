def calculate_discount(price, discount_percent):
    """Apply a discount. discount_percent is a value between 0 and 1 (e.g. 0.1 = 10%)."""
    if not 0 <= discount_percent <= 1:
        raise ValueError(f"discount_percent must be between 0 and 1, got {discount_percent}")
    discount = price * discount_percent
    return price - discount

def apply_tax(price, tax_rate):
    return price + (price * tax_rate)

if __name__ == "__main__":
    total = apply_tax(calculate_discount(100, 0.1), 0.08)
    print(f"Final price: {total}")
