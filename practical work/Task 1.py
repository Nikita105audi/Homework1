spells = []

while True:
        print("\n=== Книга заклинаний ===")
        print("1. Изучить новое заклинание")
        print("2. Показать книгу заклинаний")
        print("3. Тренироваться")
        print("4. Применить заклинание")
        print("5. Выход")

        choice = input("\nВыберите действие (1–5): ")

        if choice == "1":
            new_spell = input("Введите название нового заклинания: ")
            if new_spell:
                if new_spell in spells:
                    print(f"Заклинание '{new_spell}' уже есть в вашей книге!")
                else:
                    spells.append(new_spell)
                    print(f"Вы изучили заклинание '{new_spell}'!")
            else:
                print("Название заклинания не может быть пустым!")

        elif choice == "2":
            if spells:
                print("\nВаша книга заклинаний:")
                for i, spell in enumerate(spells, 1):
                    print(f"{i}. {spell}")
            else:
                print("Ваша книга заклинаний пуста. Изучите первое заклинание!")

        elif choice == "3":
            if not spells:
                print("У вас нет заклинаний для тренировки!")
                continue

            print("\nВыберите заклинание для тренировки:")
            for i, spell in enumerate(spells, 1):
                print(f"{i}. {spell}")

            try:
                spell_num = int(input("Номер заклинания: ")) - 1
                if 0 <= spell_num < len(spells):
                    spell = spells[spell_num]
                    print(f"\nНачинаем тренировку заклинания '{spell}'!")
                    for i in range(3):
                        print(f"Повтор {i + 1}: {spell}!")
                    print("Тренировка завершена!")
                else:
                    print("Нет такого заклинания в книге!")
            except ValueError:
                print("Введите число!")

        elif choice == "4":
            if not spells:
                print("У вас нет заклинаний!")
                continue

            target_spell = input("Какое заклинание хотите применить? ")
            if target_spell in spells:
                print(f"Вы успешно применили заклинание '{target_spell}'!")
            else:
                print(f"Вы не знаете заклинания '{target_spell}'! Изучите его сначала.")

        elif choice == "5":
            print("До новых встреч в школе магии!")
            break

        else:
            print("Пожалуйста, выберите число от 1 до 5.")







