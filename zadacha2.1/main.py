import math
import random
Simvol = input("Введите символ ожидаемой операции (+, -, /, *, ^, m(модуль), r(рандомное число), f(факторил), a(арккосинус): ")
if Simvol == "+":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a+b)
elif Simvol == "-":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a - b)
elif Simvol == "/":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if b == 0:
        print("Деление на ноль невозможно")
    else:
        print("Результат:  ", a / b)
elif Simvol == "*":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a * b)
elif Simvol == "^":
    a = float(input("Введите число: "))
    b = float(input("Введите степень: "))
    print("Результат:  ", pow(a, b))
elif Simvol == "m":
    a = float(input("Введите число: "))
    print("Результат:  ", math.fabs(a))
elif Simvol == "r":
    print("Результат:  ", random.uniform(-10000, 10000))
elif Simvol == "f":
    a = int(input("Введите число: "))
    print("Результат:  ", math.factorial(a))
elif Simvol == "a":
    a = float(input("Введите число: "))
    print("Результат:  ", math.acos(a))