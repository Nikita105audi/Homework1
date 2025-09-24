# Коэффициенты пересчёта
meter_to_miles = 0.000621371
meter_to_inches = 39.3701
meter_to_yards = 1.09361

meters = float(input("Введите количество метров: "))
print("Выберите единицу, в которую нужно перевести метры:")
print("1 - Мили")
print("2 - Дюймы")
print("3 - Ярды")

choice = input("Ваш выбор: ")

if choice == "1":
    print(f"{meters} метров = {meters * meter_to_miles} миль")
elif choice == "2":
    print(f"{meters} метров = {meters * meter_to_inches} дюймов")
elif choice == "3":
    print(f"{meters} метров = {meters * meter_to_yards} ярдов")
else:
    print("Ошибка: неизвестный выбор.")
