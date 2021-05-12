RandomNumber=int(input("Введите произвольное число: "))
BorderNumber=int(input("Введите пограничное число: "))
if RandomNumber < BorderNumber:
    print("Произвольное число меньше пограничного")
elif RandomNumber/3 >= BorderNumber:
    print("Произвольное число больше пограничного в 3 раза")
else:
    print("Произвольное число больше пограничного")
Stroka=input("Введите произвольную строку: ")
Dlina= len(Stroka)
Cimvol=False
Schet=1

for i in Stroka:
    if Schet == 'с':
        Cimvol=True
    if Schet==3:
        Schet += 1
        continue
        print(i, end="")
        Schet += 1
    if Schet==Dlina:
        Schet+=1
        continue
    print(i, end="")
    Schet+=1
if Cimvol==True:
    print("\nПрисутствует буква С")


