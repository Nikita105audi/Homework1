print("Введите любое число")
number = int(input())
print("Введите степень от 0 до  7")
a = int(input())
if a == 0:
    print(number ** 0)
elif a == 1:
    print(number ** 1)
elif a == 2:
    print(number ** 2)
elif a == 3:
    print(number ** 3)
elif a == 4:
    print(number ** 4)
elif a == 5:
    print(number ** 5)
elif a == 6:
    print(number ** 6)
elif a == 7:
    print(number ** 7)
else:
    print("Ошибка ввода операции")