# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        
        for i in range(1,len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i],1])
       
        res = ""
        for k,v in stack:
            res += k*v
        return res


s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa", 3))
        