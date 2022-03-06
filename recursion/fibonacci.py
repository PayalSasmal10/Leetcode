# 0 1 1 2 3 5 8 13 ....
# time complexity is O(2^n)
def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))


# Let's use Top down approach
def fibonacci1(n,dp):
    
    if n in [0,1]:
        return n
    if dp[n] is None:
        dp[n] = fibonacci1(n-1,dp)+fibonacci1(n-2,dp)
    return dp[n]

dp = [None] *101
print(fibonacci1(4,dp))

