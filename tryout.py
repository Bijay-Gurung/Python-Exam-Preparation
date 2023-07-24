def fib(n):
    a = 0
    b = 1
    i=0
    while i<n-1:
        c= a+b
        a=b
        b=c
        i += 1
    print(c)
fib(6)