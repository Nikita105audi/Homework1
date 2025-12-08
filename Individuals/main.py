FAILNAME = "notex.txt"
def load():
    myset = {
        {"Идея": "Сделать сюжет игры"},
        {"Покупки": "Купить молоко"},
        {"Учёба": "Сделать задание по python"},
    }

    with open("tetx.txt", "w", encoding="utf-8") as file:
        file.write(str(my_set1))

    with open("tetx.txt", "r", encoding="utf-8") as file:
        data = file.read()
        print(data)

def find_by_category(category):
    load()  
    filtered_notes = [note for note in notes if category in note]
    if filtered_notes:
        for note in filtered_notes:
            print(list(note.keys())[0], ":", list(note.values())[0])
    else:
        print(f"Заметок с категорией '{category}' не найдено.")

def search_word(word):
    if not word or not word.strip():
        return []
    
    search_key = word.strip().lower()
    result = []
    notes = load_notes()
    
    for category, text in notes:
        if search_key in category.lower() or search_key in text.lower():
            result.append((category, text))
    
    return result
          

print("1 - Добавить заметку")
print("2 - Показать все элементы")
print("3 - Найти по категориям")
print("4 - Поиск по слову")
print("5 - Выход")
choice = input("Выберите из меню: ")
if choice == "1":
    load()

elif choice == "2":
    load()

elif choice == "3":
    category = input("Введите категорию для поиска: ")
    find_by_category(category)

elif choice == "4":
    word = input("Введите слово для поиска: ").strip()
    result = search_word(word)
            
    if result:
            print(f"\nЗаметки, содержащие '{word}':")
            for cat, text in result:
                print("f!  {cat} | {text}")
            else:
                print(f"Заметок с '{word}' не найдено.")
                
elif choice == "5":
    print("До свидания!")
else:
    print("Неверный выбор. Введите число от 1 до 5.") 



 


    

