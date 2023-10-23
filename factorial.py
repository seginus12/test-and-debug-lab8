def get_factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

print(get_factorial(5))