class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        result = 0
        for i in range(1,(len(arr)+1),2):
            for j in range(0,len(arr)):
                if i+j <= len(arr):
                    for k in range(j,i+j):
                        result += arr[k]
        return result


test = Solution()
print(test.sumOddLengthSubarrays([1,4,2,5,3]))

