# инициализация переменных
try:
    k = int(input("Количество ученков в классе (целое неотрицательное число): "))
    if(k < 0):
        print("это не целое неотрицательное число")
        exit(0)
except (ValueError, EOFError):
    print("это не целое число")
    exit(0)

try:
    yearCurrent = int(input("Введите текущий год (целое неотрицательное число): "))
    if(k < 0):
        print("это не целое неотрицательное число")
        exit(0)
except (ValueError, EOFError):
    print("это не целое число")
    exit(0)

sexChild = []
yearOfBirthChild = []
ageChild = []
higthChild = []
weightChild = []

# ввод данных об учениках
for i in range(k):
    print("Ученик номер: " + str(i + 1))

    tmp = input("Пол ученика (мальчик - m/девочка - f): ")
    if (tmp != "m" and tmp != "f"):
        print("Неправильно введен пол")
        exit(0)
    sexChild.append(tmp)

    try:
        tmp = int(input("Год рождения (целое неотрицательное число): "))
        if (tmp > yearCurrent):
            print("Ребенок еще не родился")
            exit(0)
        if (k < 0):
            print("это не целое неотрицательное число")
            exit(0)
    except (ValueError, EOFError):
        print("это не целое число")
        exit(0)
    yearOfBirthChild.append(tmp)
    ageChild.append(yearCurrent - tmp)

    try:
        tmp = float(input("Рост ученика (используйте '.' для дробного числа): "))
    except (ValueError, EOFError):
        print("неверный формат числа")
        exit(0)
    higthChild.append(tmp)

    try:
        tmp = float(input("Вес ученика (используйте '.' для дробного числа): "))
    except (ValueError, EOFError):
        print("неверный формат числа")
        exit(0)
    weightChild.append(tmp)

# обработка
all = list(zip(sexChild, ageChild, higthChild, weightChild))

boys = list(filter(lambda x: x[0] == "m", all))
girls = list(filter(lambda x: x[0] == "f", all))

numberOfBoys = len(boys)
print("Мальчиков в классе: " + str(numberOfBoys))

numberOfGirls = len(girls)
print("Девочек в классе: " + str(numberOfGirls))

sum = 0
for boy in boys:
    sum += boy[1]
averageAgeBoys = sum/numberOfBoys
print("Средний возраст мальчиков в классе: " + str(averageAgeBoys))

sum = 0
for girl in girls:
    sum += girl[1]
averageAgeGirls = sum/numberOfGirls
print("Средний возраст девочек в классе: " + str(averageAgeGirls))

tmp = sorted(boys, key=lambda x: x[2], reverse = True)
if numberOfBoys > 1:
    if (tmp[0][2] > tmp[1][2] and tmp[0][3] > tmp[1][3]):
        print("Самый высокий мальчик имеет наибольший вес среди мальчиков")
    else:
        print("Самый высокий мальчик НЕ имеет наибольший вес среди мальчиков")
elif numberOfBoys == 1:
    print("В классе учиться только 1 мальчик")
else:
    print("В классе нет мальчиков")

tmp = sorted(girls, key=lambda x: x[1])
if numberOfGirls > 1:
    if(tmp[0][1] < tmp[1][1] and tmp[0][2] < tmp[1][2]):
        print("Самая юная девочка имеет наименьший вес среди девочек")
    else:
        print("Самая юная девочка НЕ имеет наименьший вес среди девочек")
elif numberOfBoys == 1:
    print("В классе учиться только 1 девочка")
else:
    print("В классе нет девочек")

# пожалуйста поправьте мой код, чтобы он стал более эффективным!