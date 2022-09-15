def binary_number (number):
    remainder = ''
    while number > 0:
        remainder = str(number % 2) + remainder
        number = number // 2
    return remainder
number = int(input('Введите число: '))
print(f'{number} -> {binary_number(number)}')