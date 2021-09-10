#Sum(n,a)-->How to calculate the sum of an array still nth elements

def sumArray(n,a):
    if n==0:
        return a[0]
    return a[n]+sumArray(n-1,a)

print(sumArray(2,[1,5,6,7,8]))