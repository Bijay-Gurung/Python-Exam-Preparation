def sumDigit(n):
    num_str = str(n)
    digit_sum = 0
    for digit in num_str:
        digit_sum += int(digit)
    return digit_sum
result = sumDigit(123)
print(result)