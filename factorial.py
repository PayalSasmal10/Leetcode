
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(6))

# 0 1 1 2 3 5 8
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))