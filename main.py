from random import randint
from typing import List


class lab1:
    @staticmethod
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

    @staticmethod
    def is_palindrome(string):
        try:
            if not isinstance(string, list):
                return string == string[::-1]
        except TypeError as error:
            return error
        else:
            return "Expected string, got array"

    @staticmethod
    def get_factorial(number):
        if isinstance(number, int):
            result = 1
            for i in range(2, number + 1):
                result *= i
            return result
        else:
            return f"Expected int, got {type(number)}"

    @staticmethod
    def get_fibonacci_number_by_position(position):
        if isinstance(position, int) and position > 0:
            num1 = 0
            num2 = 1
            if position == 1:
                return num1
            if position == 2:
                return num2
            for i in range(3, position + 1):
                sum = num1 + num2
                num1 = num2
                num2 = sum
            return sum
        else:
            return f"Expected positive int, got {type(position)}"

    @staticmethod
    def float_pow(number, power):
        if isinstance(number, float) and isinstance(power, float):
            return number ** power
        else:
            return f"Number neither power is not float"

    @staticmethod
    def is_prime(number):
        try:
            if number > 1 and not isinstance(number, float):
                for i in range(2, int(number / 2) + 1):
                    if (number % i) == 0:
                        return False
                else:
                    return True
            return False
        except TypeError as error:
            return error

