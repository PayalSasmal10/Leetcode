# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(s: str) -> int:
        strh = s.split()
        test = strh[-1]
        return len(test)

sh = Solution
print(sh.lengthOfLastWord("Hello World "))
        