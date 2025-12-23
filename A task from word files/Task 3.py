def print_matrix(matrix):
    """Вывод матрицы в удобном формате"""
    for row in matrix:
        print(" ".join(f"{x:>4}" for x in row))


def zero_out_column(matrix, col_idx):
    """Обнуляет указанный столбец (по индексу)"""
    if 0 <= col_idx < len(matrix[0]):
        for row in matrix:
            row[col_idx] = 0
        return True
    else:
        return False

def main():
    # Исходная матрица
    num = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    print("Исходная матрица:")
    print_matrix(num)
    print()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать текущую матрицу")
        print("2. Обнулить столбец")
        print("3. Выход")

        choice = input("\nВаш выбор (1–3): ").strip()

        if choice == "1":
            print("\nТекущая матрица:")
            print_matrix(num)

        elif choice == "2":
            try:
                col = int(input(f"\nВведите номер столбца (1–{len(num[0])}): ")) - 1
                if zero_out_column(num, col):
                    print(f"Столбец {col + 1} обнулён!")
                else:
                    print("Ошибка: номер столбца вне диапазона!")
            except ValueError:
                print("Ошибка: введите число!")

        elif choice == "3":
            print("До свидания!")
            break

if __name__ == "__main__":
    main()
