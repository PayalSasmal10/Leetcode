#https://leetcode.com/problems/valid-palindrome/

# 1st way using isalnum() method
class Solution:
    def isPalindrome(s: str) -> bool:
        str1 = ""
        str2 = ""
        for i in s.lower():
            if i.isalnum():
                str1 = i + str1
            
            if i.isalnum():
                str2 += i
        print(str1)
        print(str2)
        if str1 == str2:
            return True
        else:
            return False

s = Solution
print(s.isPalindrome("A man, a plan, a canal: Panama"))

# 2nd way:
class Solution2:
    
    def alphanumeric(self, st):
        if ((ord(st)>=48 and ord(st)<=57) or (ord(st) >= 65 and ord(st) <= 90) or (ord(st) >=97 and ord(st) <= 122)):
            return True
        return False
    
    def isPalindrome2(self,s: str) -> bool:
        str1 = ""
        str2 = ""
        for i in s.lower():
            if self.alphanumeric(i):
                str1 = i + str1
            if self.alphanumeric(i):
                str2 += i
        if str1 == str2:
            return True
        else:
            return False
                
s2 = Solution2
test=s2.isPalindrome2("A man, a plan, a canal: Panama")
print(test)
