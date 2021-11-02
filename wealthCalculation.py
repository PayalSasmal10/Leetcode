#https://leetcode.com/problems/richest-customer-wealth/
teswt = [[1,2,3],[4,5,6]]
maxx = 0
for i in teswt:
    maxx = max(maxx,sum(i))
print(maxx)

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:       
#         test = []
#         for i in accounts:
#             summ = 0
#             for j in i:
#                 summ += j
#             test.append(summ)
#             dec = sorted(test)
#         return dec[-1]   