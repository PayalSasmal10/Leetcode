# https://leetcode.com/problems/factorial-trailing-zeroes/
# Brute force algorithms. O(n)
# This approach is not possible for 30!

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        countt = 0
        for i in range(2,n+1):
            res *= i
        while(res>0):
            if (res %10 == 0):
                countt += 1
                res /= 10
            else:
                break
                
        return countt

s = Solution()
print(s.trailingZeroes(10))

# o(n) solution for all kind of bigger factorial

class Solution1:                
    def trailingZeroes1(self, n: int) -> int:
        ans = 0
        while(n>=5):
            n //= 5
            ans += n
        
        return ans

s1 = Solution1()
print(s1.trailingZeroes1(50))

        
