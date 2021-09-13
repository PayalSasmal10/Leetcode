# 0 1 1 2 3 5 8 13 ....
def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))



