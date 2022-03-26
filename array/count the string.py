# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        sum = 0
        
        for i in words:
            if set(i).issubset(allowed):
                sum += 1
        return sum
        
s = Solution()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))