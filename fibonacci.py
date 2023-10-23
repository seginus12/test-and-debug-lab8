def get_fibonacci_number_by_position(position):
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

print(get_fibonacci_number_by_position(10))