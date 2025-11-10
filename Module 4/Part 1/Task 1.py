line = str(input("Write text: "))
reversed = line[::-1]
print(line)
if reversed != line:
    print("Error")