# Задача 9
# Скопировать из файла F1 в файл F2 все строки, начинающиеся на букву "A", расположенные между строками с номерами N1 и N2.
# Определить количество слов в первой строке файла F2
try:
    fileInput = open("F1.txt", "r")
    #print("File " + fileInput.name + " is opened")
except FileNotFoundError:
    print ("File is not found")
except IOError:
   print("Some incorrect in reading of " + fileInput.name)

try:
    allLines = fileInput.readlines()
    fileInput.close()
except Exception:
    print("Something gone wrong during reading of " + fileInput.name)

numberLines = 0
for line in allLines:
        numberLines += 1

try:
    firstLine = int(input("Enter an integer value for the line number between 1 and " + str(numberLines) + " from which the check start:\n"))
    firstLine -=1
    if(firstLine < 0 or firstLine > numberLines):
        print("Number is incorrect")
        exit(-1)
except Exception:
    print("This is not integer value")
    exit(-1)

try:
    lastLine = int(input("Enter an integer value for the line number between " + str(firstLine + 1) + " and " + str(numberLines) + " from which the check start:\n"))
    lastLine -=1
    if(lastLine < firstLine):
        print("Number is less than than " + str(firstLine + 1))
        exit(-1)
    if (lastLine > numberLines - 1):
        print("Number is more than " + str(numberLines))
        exit(-1)
except Exception:
    print("This is not integer value")
    exit(-1)

# select strings from the list from firstLine to lastList and starting with "A"
checkLines = list((e for i, e in enumerate(allLines) if i in range(firstLine, lastLine + 1) and e[0] == "A"))

if(len(checkLines) != 0):
    fileOutput = open("F2.txt", "w")
    for item in checkLines:
        fileOutput.write("%s\n" % item)
    fileOutput.close()
    x = checkLines[0].split()
    print("Phrase:\"" + checkLines[0] + "\"" + " contains " + str(len(x)) + " words")
else:
    print("There is no any string in " + fileInput.name + " that begins with \"A\"")
