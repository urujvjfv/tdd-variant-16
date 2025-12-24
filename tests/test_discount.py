import sys
import os

# Добавляем путь к src для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from discount import calculate_discount


def test_regular_discount():
    """Тест обычной скидки"""
    assert calculate_discount(100.0, 20.0) == 80.0
    print("✓ test_regular_discount пройден")


def test_zero_discount():
    """Тест нулевой скидки"""
    assert calculate_discount(100.0, 0.0) == 100.0
    print("✓ test_zero_discount пройден")


def test_full_discount():
    """Тест 100% скидки"""
    assert calculate_discount(100.0, 100.0) == 0.0
    print("✓ test_full_discount пройден")


def test_fractional_discount():
    """Тест дробной скидки"""
    # Используем приблизительное сравнение для float
    result = calculate_discount(100.0, 25.5)
    assert abs(result - 74.5) < 0.001
    print("✓ test_fractional_discount пройден")


def test_negative_discount():
    """Тест отрицательной скидки"""
    try:
        calculate_discount(100.0, -10.0)
        assert False, "Должно было быть исключение ValueError"
    except ValueError as e:
        assert "Скидка должна быть в диапазоне от 0 до 100%" in str(e)
        print("✓ test_negative_discount пройден")


def test_discount_above_100():
    """Тест скидки больше 100%"""
    try:
        calculate_discount(100.0, 150.0)
        assert False, "Должно было быть исключение ValueError"
    except ValueError as e:
        assert "Скидка должна быть в диапазоне от 0 до 100%" in str(e)
        print("✓ test_discount_above_100 пройден")


def test_rounding():
    """Тест округления"""
    assert calculate_discount(99.99, 33.33) == 66.66
    print("✓ test_rounding пройден")


def test_edge_cases():
    """Тест граничных случаев"""
    assert calculate_discount(0.0, 50.0) == 0.0
    assert calculate_discount(50.0, 10.0) == 45.0
    assert calculate_discount(200.0, 25.0) == 150.0
    print("✓ test_edge_cases пройден")


def test_type_errors():
    """Тест ошибок типа"""
    try:
        calculate_discount("100", 20.0)
        assert False, "Должно было быть исключение TypeError"
    except TypeError:
        print("✓ test_type_errors (цена не число) пройден")
    
    try:
        calculate_discount(100.0, "20")
        assert False, "Должно было быть исключение TypeError"
    except TypeError:
        print("✓ test_type_errors (скидка не число) пройден")


def run_all_tests():
    """Запускает все тесты"""
    print("=" * 60)
    print("Запуск всех тестов")
    print("=" * 60)
    
    # Список всех тестов
    test_functions = [
        test_regular_discount,
        test_zero_discount,
        test_full_discount,
        test_fractional_discount,
        test_negative_discount,
        test_discount_above_100,
        test_rounding,
        test_edge_cases,
        test_type_errors,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"✗ {test_func.__name__} не пройден: {e}")
        except Exception as e:
            failed += 1
            print(f"✗ {test_func.__name__} вызвал исключение: {type(e).__name__}: {e}")
    
    print("\n" + "=" * 60)
    print(f"ИТОГ: {passed} пройдено, {failed} не пройдено")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
