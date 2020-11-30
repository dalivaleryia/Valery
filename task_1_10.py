try:
    n = int(input("введите целое число:\n"))
except (ValueError, EOFError):
    print("это не целое число")
    exit(0)

str = str(n)
sum = sum(map(int, list(str)))

if(sum % 3 == 0):
    print(str + " делится на 3 без остатка")
else:
    print(str + " не делится на 3 без остатка")