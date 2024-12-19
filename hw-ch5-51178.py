def fibonacci(n):
    a=0
    b=1
    if n<=0:
        return 0
    elif n==1:
        return b
    for n in range(2,n+1):
        a, b = b, a+b
    return b

