def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2) #updating n-1 by replacing n

result = fibonacci(6)
print(result)

"""
In the above code i have changes the code in 5th line. 
return fibonacci(n) + fibonacci(n-2) cause an infinite recursion. To fix it i have adjust the recursive call so, i change
it to fibonacci(n-1) + fibonacci(n-2)
"""
