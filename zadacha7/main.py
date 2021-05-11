def Dict():
    firstList = input('Введите слова через запятую: ').split(",")

    print("Количество слов в списке", len(firstList))

    secondList = input('Введите {} слов(а): '.format(len(firstList))).split(",")

    if len(firstList) != len(secondList):
        print("Количество слов в списке различается")

    return dict(zip(firstList, secondList))



fileName = input("Введите имя файла: ")
file = open(fileName, 'w')
file.write(Dict().__str__())
file.close()