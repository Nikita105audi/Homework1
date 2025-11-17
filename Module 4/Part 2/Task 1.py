exp = str(input())
sign1 = "+"
sign2 = "-"
sign3 = "*"
sign4 = "/"
if sign1 in exp:
    a,b = exp.split(sign1)
    result = float(a) + float(b)
    print(result)
elif sign2 in exp:
    a,b = exp.split(sign2)
    result = float(a) - float(b)
    print(result)
elif sign3 in exp:
    a,b = exp.split(sign3)
    result = float(a) * float(b)
    print(result)
elif sign4 in exp:
    a,b = exp.split(sign4)
    result = float(a) / float(b)
    print(result)