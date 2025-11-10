from re import split
print(sum(any(map(str.isalpha, s)) for s in split(r'[.!?]+', input())))