# https://leetcode.com/problems/reverse-string/

s = ["hi","there"]
print(s[::-1])

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
        #2nd approch
        # s.reverse()
        #3rd approach- two pointer
        # i =0
        # j = len(s)-1
        
        # while(i<=j):
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1


sw = Solution()
print(sw.reverseString(['h','e','l','l','o']))