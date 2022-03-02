# https://leetcode.com/problems/kth-distinct-string-in-an-array/submissions/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dictt = {}
        
        for i in range(len(arr)):
            countt = 0
            if arr[i] in dictt:
                dictt[arr[i]] += 1
            else:
                dictt[arr[i]] = countt+1
        
        output = [j for j in dictt if dictt[j] == 1]
        print(output)
        
        if output and len(output)>=k:
            return output[k-1]
        return ""