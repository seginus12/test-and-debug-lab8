from main import lab1
import random


class Tests:
    # insertion_sorting test
    @staticmethod
    def test_insertion_sorting_1():
        arr = [random.randint(-100, 100) for i in range(10)]
        arr_shuffled = arr
        random.shuffle(arr_shuffled)
        assert lab1.insertion_sorting(arr_shuffled) == arr

    @staticmethod
    def test_insertion_sorting_2():
        arr = [random.random() for i in range(10)]
        arr_shuffled = arr
        random.shuffle(arr_shuffled)
        assert lab1.insertion_sorting(arr_shuffled) == arr

    # is_palindrome test
    @staticmethod
    def test_check_palindrome_1():
        assert lab1.is_palindrome("POTOP") == True

    @staticmethod
    def test_check_palindrome_2():
        assert lab1.is_palindrome("aoaoaoa") == True

    @staticmethod
    def test_check_palindrome_3():
        assert lab1.is_palindrome(4) == False

    # get_factorial test
    @staticmethod
    def test_get_factorial_1():
        assert lab1.get_factorial(5) == 120

    @staticmethod
    def test_get_factorial_2():
        assert lab1.get_factorial("python kruta") == 120

    # get_fibonacci_number_by_position test
    @staticmethod
    def test_get_fibonacci_number_by_position_1():
        assert lab1.get_fibonacci_number_by_position(1) == 0

    @staticmethod
    def test_get_fibonacci_number_by_position_2():
        assert lab1.get_fibonacci_number_by_position(2) == 1

    @staticmethod
    def test_get_fibonacci_number_by_position_3():
        assert lab1.get_fibonacci_number_by_position(10) == 34

    # float_pow test
    @staticmethod
    def test_float_pow_1():
        eps = 0.00001
        assert abs(lab1.float_pow(2.4, 3.5) - 21.41604) < eps

    @staticmethod
    def test_float_pow_2():
        eps = 0.00001
        assert abs(lab1.float_pow(2.4, -3.5) - 0.04669) < eps

    # is_prime tests
    @staticmethod
    def test_is_prime_1():
        assert lab1.is_prime(281) == True

    @staticmethod
    def test_lab1_is_prime_2():
        assert lab1.is_prime(-12) == False

    @staticmethod
    def test_lab1_is_prime_3():
        assert lab1.is_prime("string") == False
