def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n-1)
result = f(5)
print(f"The output of f(5) is {result}")