# Maximum of all subarrays of size k

"""
input: [1, 3, -1, -3, 5, 3, 6, 7]
output: [3, 3, 5, 5, 6, 7] # [1, 3, -1] max of this sub array is 3, [-1, -3, 5] is 5 etc
k = 3
"""

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

class A1:
    
    def subarray(self,arr, k):
        output = []
        for i in range(len(arr)-k+1):
            max_val = arr[i]
            for j in range(i,i+k):
                if arr[j] >= max_val:
                    max_val = max(max_val, arr[j])
            
            output.append(max_val)
        return output


a = A1()
print(a.subarray(arr,k))


print("..........................................")

arr = [3, 2, 1, 5]
class A:
    def subArrays(self,arr, k):
        i = j = 0
        output = []
        max_val = arr[0]
        while(j<len(arr)):
            if arr[j] >= max_val:
                max_val = max(arr[j], max_val)
                
            
            if j-i+1 < k:
                j += 1
            
            elif j-i+1 == k:
                if arr[j] > arr[i]:
                    max_val = max(max_val, arr[j])
                output.append(max_val)
                i += 1
                j += 1
        return output


a = A()
print(a.subArrays(arr,k))

                

