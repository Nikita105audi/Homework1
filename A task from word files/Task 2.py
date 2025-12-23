import random
text = str("Это пример для задачи поэтому сдесь этот текст")
words = text.split()
random.shuffle(words)
new_text = " ".join(words)
print(new_text)