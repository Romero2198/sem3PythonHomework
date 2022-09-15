def sum_of_numbers(list_1):
    summa = 0
    for i in range(len(list_1)):
        if i % 2 != 0:
            summa += list_1[i]   
    return(summa)
list_1 = [2, 3, 5, 9, 3]
print(f'{list_1} -> {sum_of_numbers(list_1)}')