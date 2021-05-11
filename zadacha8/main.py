import module
Simvol = input("Введите символ ожидаемой операции (+, -, /, *, ^, m(модуль), r(рандомное число), f(факторил), a(арккосинус): ")

if Simvol == "+":
    module.plus()
elif Simvol == "-":
    module.minus()
elif Simvol == "/":
    module.delenie()
elif Simvol == "*":
    module.umn()
elif Simvol == "^":
    module.stepen()
elif Simvol == "m":
    module.modul()
elif Simvol == "r":
    module.rand()
elif Simvol == "f":
    module.fact()
elif Simvol == "a":
    module.arc()