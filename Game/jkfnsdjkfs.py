class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        print("Персонаж атакует!")

    def __str__(self):
        return f"Имя: {self.name}, Здоровье: {self.health}, Сила: {self.strength}"



class Warrior(Character):
    def __init__(self, name, health, strength):
        # Увеличиваем здоровье и силу воина
        super().__init__(name, health * 1.5, strength * 1.8)

    def attack(self):
        print("Воин наносит мощный удар мечом!")



class Mage(Character):
    def __init__(self, name, health, strength, mana):
        super().__init__(name, health, strength * 0.7)  # Уменьшаем силу
        self.mana = mana

    def attack(self):
        print("Маг выпускает огненный шар!")

    def __str__(self):
        return (f"Имя: {self.name}, Здоровье: {self.health}, "
                f"Сила: {self.strength}, Мана: {self.mana}")
def main():
    characters = []  # Список для хранения персонажей

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Создать персонажа")
        print("2. Показать всех персонажей")
        print("3. Атака персонажа")
        print("4. Выход")

        choice = input("\nВыберите действие (1–4): ").strip()

        if choice == "1":
            print("\nВыберите класс:")
            print("1 — Воин")
            print("2 — Маг")
            class_choice = input("Введите 1 или 2: ").strip()

            name = input("Имя персонажа: ").strip()
            health = int(input("Здоровье: "))
            strength = int(input("Сила: "))

            if class_choice == "1":
                char = Warrior(name, health, strength)
                characters.append(char)
                print(f"Воин {name} создан!\n")
            elif class_choice == "2":
                mana = int(input("Мана: "))
                char = Mage(name, health, strength, mana)
                characters.append(char)
                print(f"Маг {name} создан!\n")
            else:
                print("Неверный выбор класса.\n")

        elif choice == "2":
            if not characters:
                print("Персонажей пока нет.\n")
            else:
                print("\nСписок персонажей:")
                for i, char in enumerate(characters, 1):
                    print(f"{i}. {char}")
                print()

        elif choice == "3":
            if not characters:
                print("Нет персонажей для атаки.\n")
                continue

            print("\nВыберите персонажа для атаки:")
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char.name}")

            try:
                idx = int(input("Номер персонажа: ")) - 1
                if 0 <= idx < len(characters):
                    characters[idx].attack()
                    print()
                else:
                    print("Нет такого персонажа.\n")
            except ValueError:
                print("Введите число.\n")

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Неверный ввод. Попробуйте ещё раз.\n")



# Запуск программы
if __name__ == "__main__":
    main()
