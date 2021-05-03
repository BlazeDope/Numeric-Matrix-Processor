# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:39:16 2021

@author: sebas
"""

def create_array(i):
    array = []
    try:
        for _ in range(i[0]):
            a = input()
            temp = [float(x) for x in a.split(' ')]
            array.append(temp)
    except ValueError:
        print('Please enter again')
        create_array()
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
        string += '\n'
    return string


def main_menu():
    print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices'
          '\n0. Exit')
    i = input('Your choice: ')
    return i


def multiply(arr1, arr2):
    if len(arr1[0]) == len(arr2):
        return [[sum(x * y for x, y in zip(a, c)) for c in zip(*arr2)] for a in arr1]
    else:
        return False


def short():
    inp = list(map(int, input('Enter size of first matrix: ').split()))
    print('Enter first matrix:')
    arr = create_array(inp)
    inp2 = list(map(int, input('Enter size of second matrix: ').split()))
    print('Enter second matrix:')
    arr2 = create_array(inp2)
    return arr, arr2


def main():
    while True:
        ans = main_menu()

        if ans == '1':
            arrays = short()
            arr_sum = sum_array(arrays[0], arrays[1])
            if not arr_sum:
                print('The operation cannot be performed.\n')
            else:
                print('The result is:\n')
                print(stringify(arr_sum))

        elif ans == '2':
            inp = list(map(int, input('Enter size of matrix: ').split()))
            print('Enter matrix:')
            arr = create_array(inp)
            inp2 = int(input('Enter constant: '))
            mul = mult_k(arr, inp2)
            print('The result is:\n')
            print(stringify(mul))

        elif ans == '3':
            arrays = short()
            m = multiply(arrays[0], arrays[1])
            if not m:
                print('The operation cannot be performed.\n')
            else:
                print('The result is:\n')
                print(stringify(m))

        elif ans == '0':
            break


if __name__ == '__main__':
    main()