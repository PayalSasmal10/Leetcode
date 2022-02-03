class Solution:
    def isValid(s: str) -> bool:
        if len(s)%2 != 0:
            return 0
        dictt = {'(':')','[':']','{':'}'}
        satckk = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                satckk.append(i)
            elif len(satckk) == 0 or i != dictt[satckk[-1]]:
                return 0
            else:
                satckk.pop()
        if len(satckk) > 0:
            return 0
        return 1

s = Solution
print(s.isValid("{}[]"))





