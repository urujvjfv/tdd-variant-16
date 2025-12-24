#!/usr/bin/env python3
"""
Главный файл для запуска проекта
"""

import sys
import os

def main():
    print("=" * 60)
    print("TDD ЛАБОРАТОРНАЯ РАБОТА - ВАРИАНТ 16")
    print("=" * 60)
    
    print("\nВыберите действие:")
    print("1. Запустить демонстрацию работы функции")
    print("2. Запустить все тесты")
    print("3. Выход")
    
    choice = input("\nВведите номер (1-3): ").strip()
    
    if choice == "1":
        print("\nЗапуск демонстрации...")
        from src.discount import run_examples
        run_examples()
        
        # Интерактивный режим
        print("\nИнтерактивный режим:")
        print("-" * 40)
        while True:
            try:
                price_input = input("\nВведите цену (или 'q' для выхода): ").strip()
                if price_input.lower() == 'q':
                    break
                
                discount_input = input("Введите процент скидки (0-100): ").strip()
                if discount_input.lower() == 'q':
                    break
                
                price = float(price_input)
                discount = float(discount_input)
                
                from src.discount import calculate_discount
                result = calculate_discount(price, discount)
                
                print(f"\nРезультат: {price:.2f} руб. - {discount}% = {result:.2f} руб.")
                discount_amount = price - result
                print(f"Скидка составила: {discount_amount:.2f} руб.")
                
            except ValueError as e:
                print(f"Ошибка: {e}")
            except TypeError as e:
                print(f"Ошибка типа: {e}")
            except KeyboardInterrupt:
                print("\nВыход из программы.")
                break
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
    
    elif choice == "2":
        print("\nЗапуск тестов...")
        # Добавляем путь для импорта
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        
        # Запускаем тесты
        result = os.system("python -m pytest tests/ -v")
        if result != 0:
            print("\nНекоторые тесты не прошли!")
        else:
            print("\nВсе тесты прошли успешно!")
    
    elif choice == "3":
        print("\nВыход из программы.")
        sys.exit(0)
    
    else:
        print("\nНеверный выбор. Пожалуйста, введите 1, 2 или 3.")
    
    print("\n" + "=" * 60)
    print("Программа завершена")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        sys.exit(0)
