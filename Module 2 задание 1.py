a = int(input())
b = int(input())
c = int(input())
choice = str(input("Ведите sum для суммирования или multiply для умножения"))
if choice == "sum":
    print(a + b + c)
elif choice == "multiply":
    print(a * b * c)