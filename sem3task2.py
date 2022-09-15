def mult_of_numbers(list_1):
    mult = 0
    res_list = []
    for i in range(len(list_1) - 2):
        mult = list_1[i] * list_1[-i - 1]
        res_list.append(mult)
    return(res_list)
list_1 = [2, 3, 5, 6]
print(f'{list_1} -> {mult_of_numbers(list_1)}')
