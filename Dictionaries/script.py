goods = ["Фрукты", 'Овощи']
products = {
    "Фрукты": [("Яблоко", 15, 60), ("Бананы", 10, 80)],
    "Овощи": [("Морковь", 20, 30)]
}

total_sum = 0

for category in goods:

    for product in products[category]:
        name, quantity, price_per_unit = product

        current_product_total = quantity * price_per_unit

        total_sum += current_product_total

        print(
            f"{category}: {name}, Количество: {quantity}, Цена за ед.: {price_per_unit}, Итого: {current_product_total}")

print(f"\nОбщая сумма всех товаров: {total_sum}")
productc = max(products, key=products.get)
print(f"Самый дорогой товар: {productc}")
max_tovari = max(len(kategorii) for kategorii in products.values())

kategorii = [k for k, v in products.items() if len(v) == max_tovari]

print(f"Категория с наибольшим количеством товаров: {kategorii}")