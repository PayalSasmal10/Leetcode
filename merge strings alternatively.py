# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word3 = ""
        while(i<len(word1) and i < len(word2)):
            word3 += word1[i]+word2[i]
            i += 1
            
        word3 += word1[i:]+word2[i:]
        return word3

s = Solution()
print(s.mergeAlternately("ab", "pqrs"))