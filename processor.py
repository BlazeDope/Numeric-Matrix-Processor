# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:39:16 2021

@author: sebas
"""

def create_array(i):
    array = []
    for _ in range(i[0]):
        a = input()
        temp = [int(x) for x in a.split(' ')]
        array.append(temp)
    return array


def sum_array(array1, array2):
    array = []
    if len(array1) == len(array2) and len(array1[0]) == len(array2[0]):
        for i in range(len(array1)):
            temp = [array1[i][j] + array2[i][j] for j in range(len(array1[0]))]
            array.append(temp)
        return array
    else:
        return False


def mult_k(array, c):
    result = []
    try:
        for i in range(len(array)):
            temp = [c * array[i][j] for j in range(len(array[0]))]
            result.append(temp)
    except TypeError:
        temp = [c * array[j] for j in range(len(array))]
        result.append(temp)
    return result



def stringify(array):
    string = ''
    for i in range(len(array)):
        for j in range(len(array[0])):
            string += f' {str(array[i][j])}'
            string = string.lstrip()
        string += '\n'
    return string


def main():
    inp = list(map(int, input().split()))
    arr = create_array(inp)
    inp2 = list(map(int, input().split()))
    if len(inp2) >= 2:
        arr2 = create_array(inp2)
        arr_sum = sum_array(arr, arr2)
        if not arr_sum:
            print('ERROR')
        else:
            print(stringify(arr_sum))
    elif len(inp2) == 1:
        mul = mult_k(arr, inp2[0])
        print(stringify(mul))


if __name__ == '__main__':
    main()