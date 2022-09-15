from math import floor
from unittest import skip
def convert_to_fractional (list_1):
    for i in list_1:
        fractional = round(i - floor(i),2)
        if fractional == 0:
            skip
        else:
            list_2.append(fractional)
    return(list_2)
def find_max_number(list_2):
    max_number = list_2[0]
    for i in list_2:
        if i > max_number:
            max_number = i
    return(max_number)
def find_min_number(list_2):
    min_number = list_2[0]
    for i in list_2:
        if i < min_number:
            min_number = i
    return(min_number)
list_1 = [1.1, 1.2, 3.1, 5, 10.01]
list_2 = []
convert_to_fractional(list_1)
print(f'{list_2} => {(find_max_number(list_2)) - (find_min_number(list_2))}')



