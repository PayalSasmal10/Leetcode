# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in s:
            if stack:
                if i == stack[-1]:
                    print("before:",stack)
                    stack.pop()
                    print(stack)
                    continue            
            print("I am here", i)
            stack.append(i)
            
        return "".join(stack)


s = Solution()
print(s.removeDuplicates("abbaca"))


