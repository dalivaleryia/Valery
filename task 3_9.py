# Среднее арифметическое
import random

A = []
try:
    n = int(input("введите целое число:\n"))
except (ValueError, EOFError):
    print("это не целое число")
    exit(0)

for i in range(n):
    a = random.randint(0, 99)
    A.append(a)

numbers_sum = sum(A)
result = numbers_sum/n
print(result)