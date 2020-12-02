height = int(input("1 сторона прямоугольника: "))
width = int(input("2 сторона прямоугольника: "))

if height > width:
    height, width = width, height

numberRec = 0

#рекурсивная функция для подсчета количества квадратов в прямоугольнике
def cutRectangle(a, b, resultA = []):
    global numberRec

    if a <= 0 or b <= 0:
        return
    else:
        if(a <= b):
            resultA.append(a)
            b -= a
        else:
            resultA.append(b)
            a -= b
        numberRec += 1
        cutRectangle(a, b)
    return resultA

resultA = cutRectangle(height, width)
print(numberRec)
print(resultA)

resultANumbers = list(map(lambda x: x*x, resultA))

length = len(resultA)

row = []
correctorPrintingChar = 0 # Цикл для печати от "A" до "Z"
for i in range(height):
    column = width
    for k in range(length):
        if resultANumbers[k] != 0:
            for j in range(resultA[k]):
                if k > 25:
                    correctorPrintingChar = 25
                else:
                    correctorPrintingChar = 0
                row.append(chr(65 + k - correctorPrintingChar))
            resultANumbers[k] = resultANumbers[k] - resultA[k]
            column -= resultA[k]
            if column == 0:
                break
    print(str(row)[1:-1])
    row = []