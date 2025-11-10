text = str(input("Введите текст: ")).lower().split()
word = str(input("Введите зарезервированые слова: ")).lower().split()
for i, w in enumerate(text):
    if w in word:
        text[i] = w.upper()
        print(" ".join(text))


