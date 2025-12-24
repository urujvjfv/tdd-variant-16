def calculate_discount(price, discount_percent):
    """
    Рассчитывает итоговую цену после применения скидки.
    
    Аргументы:
        price: исходная цена (float или int)
        discount_percent: процент скидки от 0 до 100 (float или int)
    
    Возвращает:
        Итоговая цена после скидки, округленная до 2 знаков
    
    Исключения:
        ValueError: если скидка отрицательная или больше 100%
    """
    # Проверяем входные данные
    if not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом")
    if not isinstance(discount_percent, (int, float)):
        raise TypeError("Процент скидки должен быть числом")
    
    # Проверяем диапазон скидки
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")
    
    # Рассчитываем скидку
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    # Округляем до 2 знаков после запятой
    return round(final_price, 2)


# Дополнительная функция для демонстрации
def run_examples():
    """Запускает примеры использования функции"""
    print("=" * 60)
    print("Примеры работы функции calculate_discount")
    print("=" * 60)
    
    examples = [
        (100.0, 20.0, 80.0, "Обычная скидка 20%"),
        (100.0, 0.0, 100.0, "Нулевая скидка"),
        (100.0, 100.0, 0.0, "Скидка 100%"),
        (99.99, 33.33, 66.66, "Дробный процент"),
        (0.0, 10.0, 0.0, "Цена 0"),
        (100.0, 50.5, 49.5, "Скидка 50.5%"),
    ]
    
    for price, discount, expected, desc in examples:
        try:
            result = calculate_discount(price, discount)
            status = "✓" if abs(result - expected) < 0.01 else "✗"
            print(f"{status} {desc}:")
            print(f"  Цена: {price}, Скидка: {discount}% = {result} (ожидалось: {expected})")
        except Exception as e:
            print(f"✗ {desc}: Ошибка - {e}")
        print()
    
    print("\nПроверка ошибок:")
    print("-" * 40)
    
    error_cases = [
        (100.0, -10.0, "Отрицательная скидка"),
        (100.0, 150.0, "Скидка > 100%"),
        ("100", 20.0, "Нечисловая цена"),
        (100.0, "20", "Нечисловая скидка"),
    ]
    
    for price, discount, desc in error_cases:
        try:
            result = calculate_discount(price, discount)
            print(f"✗ {desc}: ОШИБКА! Должно было быть исключение")
        except (ValueError, TypeError) as e:
            print(f"✓ {desc}: Правильно вызвано исключение - {type(e).__name__}: {e}")
        print()


if __name__ == "__main__":
    run_examples()
