def main():
    # Запрашиваем длину линии
    while True:
        try:
            length = int(input("Введите длину линии: "))
            if length <= 0:
                print("Длина линии должна быть положительным числом. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

    # Запрашиваем символ для заполнения
    symbol = input("Введите символ для заполнения линии: ")

    # Выводим вертикальную линию
    for _ in range(length):
        print(symbol)

if __name__ == "__main__":
    main()
