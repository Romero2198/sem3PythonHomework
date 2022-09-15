def fibonacci_positive_numbers(list_1):
    summa = 0
    for i in range(3, k+1):
        summa = list_1[i - 1] + list_1[i - 2]
        list_1.append(summa)
    return(list_1)
def fibonacci_negative_numbers(list_1):
    summa = 0
    for i in range(k):
        summa = -(list_1[0]) + list_1[1]
        list_1.insert(0, summa)
    return(list_1)
k = int(input('Введите число: '))
list_1 = [0, 1, 1]
fibonacci_positive_numbers(list_1)
fibonacci_negative_numbers(list_1)
print(f'{k} -> {list_1}')
