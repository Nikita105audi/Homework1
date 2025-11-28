goods = {
    "Телефон2": frozenset(("техника", "электроника")),
    "Самурайский меч": frozenset(("редкое", "оружие")),
}

def find_by_category(category):
    return {good for good, categories in goods.items() if category in categories}


while True:
    print("\nМеню:")
    print("1. Добавить новый товар")
    print("2. Вывести все товары")
    print("3. Найти товары по категории")
    print("4. Выход")
    choice = input("Выберите действие (1-4): ")

    if choice == "1":
        new_good = input("Название нового товара: ")
        categories_input = input("Категории через запятую: ").split(',')
        new_goods = frozenset(map(str.strip, categories_input))
        print(f"Товар '{new_good}' успешно добавлен.")

    elif choice == "2":
        sorted_goods = sorted(goods.keys(), key=lambda x: len(x))
        for good in sorted_goods:
            print(f"{good}: {goods[good]}")

    elif choice == "3":
        search_category = input("Введите категорию для поиска: ")
        found_goods = find_by_category(search_category)
        if found_goods:
            print(f"Товары в категории '{search_category}': {found_goods}")
        else:
            print(f"В категории '{search_category}' ничего не найдено.")

    elif choice == "4":
        print("Всего доброго!")
        break
    else:
        print("Ошибка выбора. Повторите попытку.")