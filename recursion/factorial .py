# factorial without recursion
# O(n)

class Solution:
    def fact(self,n):
        res = 1

        for i in range(2,n+1):
            res *= i
        return res


s = Solution()
print(s.fact(5))


#factorial with recursion 

class solution1:
    def fact1(self, n):
        if n < 2:
            return 1
        return n*self.fact1(n-1)


s1 = solution1()
print(s1.fact1(6))