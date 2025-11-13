from re import split

text = str(input())

words = [word for word in text.split() if word.strip()]
word_count = len(words)

char_count = len(text)

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"

vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

longest = max(words, key=len) if words else ""


print(f"Количество слов: {word_count}")
print(f"Количество символов (с пробелами и знаками): {char_count}")
print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
print(f"Самое длинное слово: {longest}")
