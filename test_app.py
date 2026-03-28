from app import calculate_discount, apply_tax

def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90.0
    assert calculate_discount(200, 0.5) == 100.0
    assert calculate_discount(100, 0) == 100.0

def test_invalid_discount_percent():
    try:
        calculate_discount(100, 10)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_apply_tax():
    assert apply_tax(100, 0.08) == 108.0

def test_full_pipeline():
    assert apply_tax(calculate_discount(100, 0.1), 0.08) == 97.2

if __name__ == "__main__":
    test_calculate_discount()
    test_invalid_discount_percent()
    test_apply_tax()
    test_full_pipeline()
    print("All tests passed.")

def test_apply_tax_invalid():
    try:
        apply_tax(100, 1.5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    try:
        apply_tax(-10, 0.08)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
