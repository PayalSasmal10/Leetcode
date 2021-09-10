#How to iterate without using loops.
def recur(n):
    if n == 0:
        return 
    else:
        recur(n-1)
        print(n)


recur(5)


