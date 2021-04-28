def create_array():
    array = []
    inp = input()
    rowcol = [int(x) for x in inp.split(' ')]
    for _ in range(rowcol[0]):
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


def stringify(array):
    string = ''
    for i in range(len(array)):
        for j in range(len(array[0])):
            string += f'" "{str(array[i][j])}'
        string += '\n'
    return string

def main():
    cond = True
    while cond:
        arr = create_array()
        arr2 = create_array()
        gg = sum_array(arr, arr2)
        if not gg:
            cond = gg
            return 'ERROR'
        else:
            print(gg)


if __name__ == '__main__':
    main()