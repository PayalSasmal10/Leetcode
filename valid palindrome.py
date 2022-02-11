#https://leetcode.com/problems/valid-palindrome/

from string import digits


class Solution:
    def isPalindrome(s: str) -> bool:
        str1 = ""
        str2 = ""
        for i in s.lower():
            if i.isalnum():
                str1 = i + str1
            
            if i.isalpha() or i.isdigit():
                str2 += i
        print(str1)
        print(str2)
        if str1 == str2:
            return True
        else:
            return False

s = Solution
print(s.isPalindrome("A man, a plan, a canal: Panama"))
                
        