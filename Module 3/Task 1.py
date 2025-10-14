number1 = int(input())
number2 = int(input())
numbers = range(number1, number2+1)
sum2 = 0
count2 = 0
sum3 = 0
count3 = 0
sum_num = 0
count_num = 0
sum9 = 0
count9 = 0
for number in numbers:
    if number % 2 == 0:
        sum2 += number
        count2 += 1
    elif number % 2 != 0:
        sum3 += number
        count3 += 1

    if number % 9 == 0:
        sum9 += number
        count9 += 1
    print(sum2/count2)
    print(sum3/count3)
    print(sum9/count9)