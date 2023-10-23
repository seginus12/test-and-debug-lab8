from random import randint

LENGTH = 10
MIN_VALUE = -100
MAX_VALUE = 100


def insertion_sorting(array):
    # if any([not isinstance(elem, int) or elem is None for elem in array]):
    #     raise TypeError
    try:
        for i in range(1, len(array)):
            key = array[i]
            j = i
            while j > 0 and array[j - 1] > key:
                array[j] = array[j - 1]
                j -= 1
            array[j] = key
    except TypeError as error:
        return error
    else:
        return array


arr = [randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]
print(arr)
print(insertion_sorting(arr))
