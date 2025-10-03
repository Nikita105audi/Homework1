word = input("Напишите слово: ")
if word[-1] == "ь":
    print(word[-2])
else:
    print(word[-1])