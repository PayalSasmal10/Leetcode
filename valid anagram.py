# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        
        dictt1 = {}
        dictt2 = {}
        for i in range(len(s)):
            if s[i] in dictt1:
                dictt1[s[i]] += 1
                
            else:
                dictt1[s[i]] = 1
                
        for j in range(len(t)):
            if t[i] in dictt2:
                dictt2[t[i]] += 1
            else:
                dictt2[t[i]] =  1
        
        print(dictt1)       
        print(dictt2)       
        if dictt1 != dictt2:
            return False
        
        return True
            
s = Solution()
print(s.isAnagram("anagram", "nagaram"))
