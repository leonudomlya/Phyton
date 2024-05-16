squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

squares = [i ** 2 for i in range(10)]
print(squares)

even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i ** 2)
print(even_squares)

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)

arr = []
for x in range(6):
    if x % 2 == 0:
        arr.append('четное')
    else:
        arr.append('нечетное')
print(arr)

arr = ['четное' if x % 2 == 0 else 'нечетное' for x in range(6)]
print(arr)
print(', '.join(arr))

a = [int(x) for x in input('Введите числа через пробел: ').split()]
print(a)
evil, good = [int(x) for x in '666 777'.split()]
print(evil, good, sep='\n')

print(', '.join(str(i) + '^2=' + str(i ** 2) for i in range(1, 10)))