# T(n) = T(n-1) + T(n-2) + T(n-3), for n > 3

class RangeIterator:
    def __init__(self, size):
        self.__x = 0
        self.__size = size
        self.__a = 0
        self.__b = 0
        self.__c = 1

    def __next__(self):
        self.__x += 1
        self.__a, self.__b, self.__d = self.__b, self.__c, self.__a + self.__b + self.__c
        self.__c = self.__d
        if self.__x > self.__size:
            raise StopIteration
        return self.__d

class RangeIterable:
    def __init__(self, size):
        self.__size = size

    def __iter__(self):
        return RangeIterator(self.__size)

print("0\n0\n1")
main_iter = RangeIterable(32)
for line in main_iter:
    print(line)