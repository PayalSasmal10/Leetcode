# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        rev=0
        flag = False
        
        if x < 0:
            flag = True
            x = -x
        
        while x>0:
            rem = x%10
            rev = rev*10+rem
            if rev >= (2**31)-1 or x <= -2**31:
                return 0
            x = int(x/10)
            
        return rev if not flag else -rev
        
    
a = Solution()
print(a.reverse(1534236469))

