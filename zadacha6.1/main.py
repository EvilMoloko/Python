import math
import random
Simvol = input("Введите символ ожидаемой операции (+, -, /, *, ^, m(модуль), r(рандомное число), f(факторил), a(арккосинус): ")

def plus():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a + b)

def minus():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a-b)

def delenie():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if b == 0:
        print("Деление на ноль невозможно")
    else:
        print("Результат:  ", a/b)

def umn():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Результат:  ", a*b)

def stepen():
    a = float(input("Введите число: "))
    b = float(input("Введите степень: "))
    print("Результат:  ", pow(a, b))

def modul():
    a = float(input("Введите число: "))
    print("Результат:  ", math.fabs(a))

def rand():
    print("Результат:  ", random.uniform(-10000, 10000))

def fact():
    a = int(input("Введите число: "))
    print("Результат:  ", math.factorial(a))

def arc():
    a = float(input("Введите число: "))
    print("Результат:  ", math.acos(a))

if Simvol == "+":
    plus()
elif Simvol == "-":
    minus()
elif Simvol == "/":
    delenie()
elif Simvol == "*":
    umn()
elif Simvol == "^":
    stepen()
elif Simvol == "m":
    modul()
elif Simvol == "r":
    rand()
elif Simvol == "f":
    fact()
elif Simvol == "a":
    arc()