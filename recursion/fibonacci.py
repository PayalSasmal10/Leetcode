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
print(fibonacci1(50,dp))

# Bottom top approach - time complexity o(n)

def fibonacci2(n):
    dp1 = [0]*(n+1)
    dp1[0] = 0
    dp1[1] = 1

    for i in range(2,n):
        dp1[i] = dp1[i-1] + dp1[n-2]

    return dp1[n]

print(fibonacci2(50))




