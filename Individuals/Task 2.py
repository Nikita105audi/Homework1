from datetime import datetime

input_date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")

try:
    date_obj = datetime.strptime(input_date_str, '%Y-%m-%d')
    day_number = date_obj.weekday()
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"День недели: {days[day_number]}")
except ValueError:
    print("Неверный формат даты!")