# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        convert_to_list = list(s)
        vowels = "aeiouAEIOU"
        i = 0
        j = len(s) - 1
        
        while(i<j):
            if convert_to_list[i] in vowels and convert_to_list[j] in vowels:
                temp = convert_to_list[i]
                convert_to_list[i] = convert_to_list[j]
                convert_to_list[j] = temp
                i += 1
                j -= 1
            
            elif convert_to_list[i] in vowels and convert_to_list[j] not in vowels:
                j -= 1
            
            elif convert_to_list[i] not in vowels and convert_to_list[j] in vowels:
                i += 1
            
            else:
                i += 1
                j -= 1
        
        return ''.join(convert_to_list)
                
                
                
                
so = Solution()
print(so.reverseVowels("hello"))