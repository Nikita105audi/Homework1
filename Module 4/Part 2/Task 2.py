import random

# Создаем список случайных чисел
numbers = [random.randint(-10, 10) for _ in range(20)]

print("Список чисел:", numbers)

# Используем встроенные функции и генераторы
min_element = min(numbers)
max_element = max(numbers)
negative_count = sum(1 for num in numbers if num < 0)
positive_count = sum(1 for num in numbers if num > 0)
zero_count = sum(1 for num in numbers if num == 0)

# Выводим результаты
print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
print(f"Количество отрицательных элементов: {negative_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zero_count}")